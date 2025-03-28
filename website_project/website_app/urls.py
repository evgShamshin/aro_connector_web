from django.urls import path, register_converter
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('bim/', views.bim_page, name='bim'),
    path('it/', views.it_page, name='it'),
    path('design/', views.design_page, name='design'),
    path('projects/', views.projects_page, name='projects'),
    path('connector/', views.connector_page, name='connector'),
]