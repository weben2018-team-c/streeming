from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


@login_required()
def show_profile(request):
    user = request.user
    context = {
        'user': user,
    }
    template = loader.get_template('accounts/profile.html')
    return HttpResponse(template.render(context, request))
