from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):  # HttpResponse
    return HttpResponse('Главная страница сайта')


def categories(request):
    return HttpResponse('Категории сайта')