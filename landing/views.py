from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from .models import Releases, Users
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
        artist = Users.objects.get(id=artist_id)
        releases = Releases.objects.filter(user__id=artist_id)
        context = {
            'artist': artist,
            'releases': releases
        }
        template = loader.get_template('landing/artist.html')
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/")
