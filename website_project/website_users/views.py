from django.contrib.auth import logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from website_app.utils import DataMixin
from website_users.forms import RegisterUserForm, ProfileUserForm, PasswordChangeUserForm


class LoginPageUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    descr = 'BIM-консалтинг'


def logout_user(request):
    logout(request)
    return redirect('connector')


def register_user_done(request):
    return render(request, 'users/register_done.html')


class RegisterPageUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register_done')


class ProfilePageUser(DataMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'users/profile.html'
    form_class = ProfileUserForm

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class PasswordChangePageUser(DataMixin, PasswordChangeView):
    model = get_user_model()
    template_name = 'users/password_change.html'
    form_class = PasswordChangeUserForm
    success_url = reverse_lazy('users:password_change_done')
