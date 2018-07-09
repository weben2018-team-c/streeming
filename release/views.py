from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from release.models import Releases


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
