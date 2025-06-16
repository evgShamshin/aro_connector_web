from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect

from website_app.utils import DataMixin


class LoginPageUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    descr = 'BIM-консалтинг'


def logout_user(request):
    logout(request)
    return redirect('connector')
