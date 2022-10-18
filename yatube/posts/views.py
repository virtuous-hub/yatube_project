from django.shortcuts import render

# Create your views here.
# yatube/views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse(f'Новости на сегодня')

