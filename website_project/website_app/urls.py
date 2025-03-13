from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.by_index),
    path('cats/', views.by_categories),
    path('about/', views.by_about),
    path('slug/<slug:par_slug>/', views.by_slug, name='par_slug'),
    path('id/<int:par_id>/', views.by_id, name='par_id'),
    path('archive/<year4:year>/', views.by_archive),
]
