from django.urls import path, register_converter
from . import views

# register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.main_page, name='home'),
    path('category/<int:par_id>/', views.category_page, name='category'),
    path('project/', views.project_page, name='project'),
    path('services/', views.services, name='services'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('authorization/', views.authorization, name='authorization'),
]