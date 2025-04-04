from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from .models import WebsiteApp

about = [{'title': 'BIM', 'title_url': 'bim'},
         {'title': 'IT', 'title_url': 'it'},
         {'title': 'Design', 'title_url': 'design'},
         {'title': 'Projects', 'title_url': 'projects'},
         {'title': 'Connector', 'title_url': 'connector'}, ]

payment = [['Помощь сайту:', 'Ссылка'], ['Номер карты:', '1234567890098765']]

# cats = [{'title': 'Выгрузчик', 'par_id': '-',
#          'description': '-'},
#         {'title': 'Ключи исключения', 'par_id': '-',
#         'description': '-'},
#         {'title': 'Потолок по помещению', 'par_id': '-',
#         'description': '-'},
#         {'title': 'Замена размеров', 'par_id': '-',
#         'description': '-'},
#         {'title': 'Выгрузка координат', 'par_id': '-',
#          'description': '-'},
#         {'title': 'NotionSync', 'par_id': '-',
#          'description': '-'},
#         {'title': 'Запись параметров', 'par_id': '-',
#          'description': '-'},
#         {'title': 'Развертки помещений', 'par_id': '-',
#          'description': '-'},
#         {'title': 'Обновить из солида', 'par_id': '-',
#          'description': '-'},
#         ]

cats = WebsiteApp.objects.all()


# Create your views here.
def main_page(request: HttpRequest):  # HttpResponse
    # return HttpResponse('Главная страница сайта')
    data = {'title': 'Главная страница сайта',
            'about': about,
            'payment': payment,
            'cats': cats}
    return render(request, 'website_app/main.html', context=data)


def bim_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('BIM')


def it_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('IT')


def design_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Design')


def projects_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Projects')


def connector_page(request: HttpRequest, article_slug) -> HttpResponse:
    return HttpResponse(article_slug)


def authorization_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Авторизация')


def nof_found_page(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>\n'
                                '<h3>Проверьте доступные url адреса в .urls</h3>')
