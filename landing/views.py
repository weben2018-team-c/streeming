from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from .models import Releases, Users, Subscribes
from streeming.settings import TRACKS_LIMIT


def index(request):
    releases = Releases.objects.filter(enabled=True).order_by('updated_at').reverse()[:TRACKS_LIMIT]
    context = {
        'releases': releases
    }
    template = loader.get_template('landing/index.html')
    return HttpResponse(template.render(context, request))


def show_artist_detail(request):
    if 'artist_id' in request.GET:
        artist_id = request.GET.get('artist_id')
        # if not existing artist then go to top page
        try:
            artist = Users.objects.get(id=artist_id)
        except Users.DoesNotExist:
            return redirect('/')
        releases = Releases.objects.filter(user__id=artist_id)

        user = request.user
        print(user.id)
        if user.id:
            subscribed= Subscribes.objects.filter(user_id=user.id, artist=artist_id).exists()
        else:
            subscribed = False

        context = {
            'artist': artist,
            'releases': releases,
            'subscribed': subscribed
        }
        template = loader.get_template('landing/artist.html')
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/')
