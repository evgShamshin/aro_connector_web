from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound

about = [{'title': 'Главная', 'title_url': 'main'},
         {'title': 'Услуги', 'title_url': 'services'},
         {'title': 'FAQ', 'title_url': 'faq'},
         {'title': 'Контакты', 'title_url': 'contact'},
         {'title': 'Войти', 'title_url': 'authorization'}, ]

payment = [['Помощь сайту:', 'Ссылка'], ['Номер карты:', '1234567890098765']]

cats = [{'title': 'Проверка модели параметров', 'par_id': 1,
         'description': 'Проверяет наличие заданных параметров и создаёт отчёт в Excel с основными '
                        'показателями модели'},
        {'title': 'Проверка координат', 'par_id': 2,
         'description': 'Проверяет корректность координат в текущей или заданных моделях и создаёт отчёт в Excel'}]


# Create your views here.
def main_page(request: HttpRequest):  # HttpResponse
    # return HttpResponse('Главная страница сайта')
    data = {'title': 'Главная страница сайта',
            'about': about,
            'payment': payment,
            'cats': cats}
    return render(request, 'website_app/main.html', context=data)


def category_page(request: HttpRequest, par_id: int) -> HttpResponse:
    return render(request, 'website_app/category.html',
                  context={'par_id': par_id, 'about': about, 'payment': payment, 'cats': cats})


def project_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Проекты')


def services(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Услуги')


def faq(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Часто задаваемые вопросы')


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Контакты')


def authorization(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Авторизация')


def page_nof_found(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>\n'
                                '<h3>Проверьте доступные url адреса в .urls</h3>')
