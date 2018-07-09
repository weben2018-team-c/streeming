from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {
    }
    template = loader.get_template('landing/index.html')
    return HttpResponse(template.render(context, request))