from django.shortcuts import redirect
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('/connector/')),
    path('connector/', views.connector_page, name='connector'),
    path('connector/<slug:article_slug>/', views.connector_commands_page, name='connector_commands'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)