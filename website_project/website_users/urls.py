from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginPageUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterPageUser.as_view(), name='register'),
    path('register/done', views.register_user_done, name='register_done'),
    path('reset_password/', views.PasswordChangePageUser.as_view(), name='password_reset'),
    # path('reset_password/done', views.PasswordChangeDonePageUser.as_view(), name='password_reset_done'),
    path('reset_password/done', PasswordChangeDoneView.as_view(template_name="users/password_reset_done.html"),
         name="password_reset_done"),
    path('profile/', views.ProfilePageUser.as_view(), name='profile'),
]
