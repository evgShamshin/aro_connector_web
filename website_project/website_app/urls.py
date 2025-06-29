from xml.etree.ElementInclude import include

from django.shortcuts import redirect
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  # path("", include('social_django.urls', namespace="social")),
                  path('', lambda request: redirect('/connector/')),
                  path('connector/', views.ConnectorPage.as_view(), name='connector'),
                  path('consulting/', views.ConsultingPage.as_view(), name='consulting'),
                  path('connector/command/<slug:article_slug>/', views.connector_commands_page,
                       name='connector_commands'),
                  path('connector/group/<slug:group_slug>/', views.ConnectorPageByGroup.as_view(),
                       name='connector_group'),
                  path('connector/tag/<slug:tag_slug>/', views.ConnectorPageByTag.as_view(), name='connector_tag'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
