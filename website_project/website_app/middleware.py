import sys
from django.utils.termcolors import colorize


class ColoredStatusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self._log_request(request, response)
        return response

    def _log_request(self, request, response):
        status_code = response.status_code
        method = request.method
        path = request.get_full_path()

        # Определяем цвет в зависимости от статуса
        if status_code >= 500:
            color = 'red'
        elif status_code >= 400:
            color = 'magenta'
        elif status_code >= 300:
            color = 'yellow'
        elif status_code >= 200:
            color = 'green'
        else:
            color = 'white'

        # Формируем цветную строку
        colored_status = colorize(str(status_code), fg=color, opts=('bold',))
        log_message = f"[{colored_status}] {method} {path}"

        # Выводим в stderr (гарантированный вывод)
        print(log_message, file=sys.stderr)
