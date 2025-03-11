from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def index(request: HttpRequest):  # HttpResponse
    return HttpResponse('Главная страница сайта')


def categories(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Категории сайта')


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('О сайте')