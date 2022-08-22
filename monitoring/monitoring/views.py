from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


# Главная страница
def index(request):
    context = {}
    return render(request, 'monitoring/index.html', context)