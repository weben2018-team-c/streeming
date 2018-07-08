from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from release.models import Releases, Users


# Create your views here.
def index(request):
    # TODO: Auth
    request.session['user_id'] = 1

    user_id = request.session['user_id']
    releases = Releases.objects.filter(user__id=user_id)
    user = Users.objects.get(id=user_id)
    context = {
        'user': user,
        'releases': releases
    }
    template = loader.get_template('release/index.html')
    return HttpResponse(template.render(context, request))
