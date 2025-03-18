from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404, HttpResponseRedirect, \
    HttpResponsePermanentRedirect
from django.urls import reverse
from django.views.generic import TemplateView

'''class HomeView:
    def __init__(self, a, b):
        self.a = str(a)
        self.b = str(b)

    def get(self):
        return self.a + ' ' + self.b'''

'''data = {
    'title': 'Main page of website',
    'lst': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'tpl': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    'dct': {1: 2, 3: 4, 5: 6, 7: 8, 9: 10},
    'st': {1, 2, 3, 4, 5, 6, 7, 8, 9},
    'obj': HomeView(1, 2)
}'''


# Create your views here.
def by_index(request: HttpRequest):  # HttpResponse
    # return HttpResponse('Главная страница сайта')
    data = {'title': 'Главная страница сайта',
            'about': ["Проекты", "Услуги", "FAQ", "О компании"],
            'payment': [['Помощь сайту:', 'Ссылка'], ['Номер карты:', '1234567890098765']],
            'is_draft': False,
            }
    return render(request, 'website_app/home.html', context=data)


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
    if year > 2024:
        raise Http404()
    if year < 2019:
        return redirect(reverse('archive', args=[2024]))

    return HttpResponse(f'Архив {year} года ')


def page_nof_found(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>\n'
                                '<h3>Проверьте доступные url адреса в .urls</h3>')
