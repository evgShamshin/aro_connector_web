from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from website_app.utils import DataMixin
from website_users.forms import RegisterUserForm


class LoginPageUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    descr = 'BIM-консалтинг'


def logout_user(request):
    logout(request)
    return redirect('connector')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'users/register_done.html')
    else:
        form = RegisterUserForm()
        return render(request, 'users/register.html', {'form': form})
