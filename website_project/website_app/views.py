from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404


# Create your views here.
def main_page(request: HttpRequest):  # HttpResponse
    # return HttpResponse('Главная страница сайта')
    data = {'title': 'Главная страница сайта',
            'about': ["Проекты", "Услуги", "FAQ", "О компании"],
            'payment': [['Помощь сайту:', 'Ссылка'], ['Номер карты:', '1234567890098765']],
            'is_draft': False,
            }
    return render(request, 'website_app/main.html', context=data)


def category_page(request: HttpRequest, par_id: int) -> HttpResponse:
    return HttpResponse(f'Отображение команды с номером {par_id}')


def page_nof_found(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>\n'
                                '<h3>Проверьте доступные url адреса в .urls</h3>')