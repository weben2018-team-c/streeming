from django.http import HttpResponse
from django.template import loader

from release.models import Releases

TRACKS_LIMIT = 20


def index(request):
    releases = Releases.objects.filter(enabled=True).order_by('updated_at').reverse()[:TRACKS_LIMIT]
    context = {
        'releases': releases
    }
    template = loader.get_template('landing/index.html')
    return HttpResponse(template.render(context, request))