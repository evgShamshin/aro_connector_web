from django.urls import path, register_converter
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_page, name='main'),
    path('bim/', views.bim_page, name='bim'),
    path('it/', views.it_page, name='it'),
    path('design/', views.design_page, name='design'),
    path('projects/', views.projects_page, name='projects'),
    path('connector/<slug/article_slug>/', views.connector_page, name='connector'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)