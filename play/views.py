from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from .models import Subscribes, Users, Releases


@login_required
def index(request):
    user = request.user
    subscribes = Subscribes.objects.filter(user__id=user.id)
    enabled_artist_ids = subscribes.filter(enabled=True).values_list('artist_id', flat=True)
    releases = Releases.objects.filter(user__id__in=enabled_artist_ids)
    context = {
        'releases': releases,
        'subscribes': subscribes
    }
    template = loader.get_template('play/index.html')
    return HttpResponse(template.render(context, request))


@login_required
def subscribe(request):
    if request.POST['artist_id']:
        user = Users.objects.get(id=request.user.id)
        artist_id = request.POST['artist_id']

        # if not existing artist then show 404
        artist = get_object_or_404(Users, id=artist_id)

        # if already subscribed, then go to playlist
        if Subscribes.objects.filter(user_id=user.id, artist=artist_id):
            return redirect('/play')
        su = Subscribes(user=user, artist=artist)
        su.save()
        return redirect('/play')
    else:
        return redirect('/')
