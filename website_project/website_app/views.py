from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404


# Create your views here.
def by_index(request: HttpRequest):  # HttpResponse
    # return HttpResponse('Главная страница сайта')
    return render(request, 'website_app/home.html')

def by_categories(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Категории сайта')


def by_about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('О сайте')


def by_id(request: HttpRequest, par_id: int) -> HttpResponse:
    if request.POST:
        return HttpResponse(f'Страница №{par_id}')
    else:
        return HttpResponse('Не POST')


def by_slug(request: HttpRequest, par_slug: int) -> HttpResponse:
    if request.GET:
        return HttpResponse("|".join([f'{k}={v}' for k, v in request.GET.items()]))
    else:
        return HttpResponse('GET is empty')
    # return HttpResponse(f'Страница с названием {par_slug}')


def by_archive(request: HttpRequest, year: int) -> HttpResponse:
    if year < 2020 or year > 2024:
        raise Http404()

    return HttpResponse(f'Архив {year} года ')


def page_nof_found(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>\n'
                                '<h3>Проверьте доступные url адреса в .urls</h3>')