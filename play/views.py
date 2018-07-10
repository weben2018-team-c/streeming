from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import Subscribes, Users


@login_required
def index(request):
    user = request.user
    subscribes = Subscribes.objects.filter(user__id=user.id)
    context = {
        'subscribes': subscribes
    }
    template = loader.get_template('play/index.html')
    return HttpResponse(template.render(context, request))


@login_required
def subscribe(request):
    if request.POST['artist_id']:
        user = Users.objects.get(id=request.user.id)
        artist_id = request.POST['artist_id']
        artist = Users.objects.get(id=artist_id)
        su = Subscribes(user=user, artist=artist)
        su.save()
        return redirect('/play')
    else:
        return redirect('/')
