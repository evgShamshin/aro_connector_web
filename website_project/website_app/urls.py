from django.urls import path, register_converter
from . import views
from . import converters

# register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.main_page, name='home'),
    path('category/<int:par_id>/', views.category_page, name='cats'),
]