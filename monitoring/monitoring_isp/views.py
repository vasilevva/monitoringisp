from django.http import HttpResponse
from django.shortcuts import render


def monitorigisp(request):
    return HttpResponse('Список мороженого')

def monitorigisp_detail(request, pk):
    return HttpResponse(f'Судебный участок {pk}') 