from django.http import HttpResponse


def login_user(request):
    return HttpResponse("<h1>Welcome to BalakiRev!</h1>")


def logout_user(request):
    return HttpResponse("<h1>Bye from BalakiRev!</h1>")
