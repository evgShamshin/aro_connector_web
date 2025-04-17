from django.shortcuts import redirect
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('/connector/')),
    path('connector/', views.connector_page, name='connector'),
    path('connector/command/<slug:article_slug>/', views.connector_commands_page, name='connector_commands'),
    path('connector/group/<slug:group_slug>/', views.connector_page_by_group, name='connector_group'),
    path('connector/tag/<slug:tag_slug>/', views.connector_page_by_tag, name='connector_tag'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)