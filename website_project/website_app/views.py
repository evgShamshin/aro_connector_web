from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def by_index(request: HttpRequest):  # HttpResponse
    return HttpResponse('Главная страница сайта')


def by_categories(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Категории сайта')


def by_about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('О сайте')


def by_id(request: HttpRequest, par_id: int) -> HttpResponse:
    return HttpResponse(f'Страница №{par_id}')


def by_slug(request: HttpRequest, par_slug: int) -> HttpResponse:
    return HttpResponse(f'Страница с названием {par_slug}')


def by_archive(request: HttpRequest, year: int) -> HttpResponse:
    return HttpResponse(f'Архив за год {year}')