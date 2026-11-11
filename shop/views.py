from django.http import HttpResponse

def home(request):
    return HttpResponse('Главная страница')

def about(request):
    return HttpResponse('О проекте')

def contacts(request):
    return HttpResponse('Контакты')

def hello(request, name):
    return HttpResponse(f'Привет, {name}!')

def calc(request, a, b):
    return HttpResponse(f'Сумма: {a + b}<br>Разность: {a - b}<br>Произведение: {a * b}')