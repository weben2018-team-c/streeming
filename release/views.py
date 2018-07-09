from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from release.models import Releases, Tracks, Users


# Create your views here.
@login_required
def index(request):
    user = request.user
    releases = Releases.objects.filter(user__id=user.id)
    context = {
        'user': user,
        'releases': releases
    }
    template = loader.get_template('release/index.html')
    return HttpResponse(template.render(context, request))


@login_required
def register_track(request):
    user = request.user
    title = request.POST['title']
    description = request.POST['description']
    tr = Tracks(title=title, description=description)
    tr.save()
    rel = Releases(user=Users(id=user.id), track=tr)
    rel.save()
    return redirect("/release")
