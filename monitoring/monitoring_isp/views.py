from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import MonitoringIsp


def monitorigisp(request):
    page_obj = MonitoringIsp.objects.none()
    listuch =[]
    a = list(MonitoringIsp.objects.values('nomeruch').distinct())
    for x in a:
        listuch.append(*x.values())
    for x in listuch:
        findobj=MonitoringIsp.objects.filter(nomeruch=x).latest('monitoringdata') 
        page_obj |= MonitoringIsp.objects.filter(pk = findobj.pk)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'monitoring_isp/monitorigisp.html', context)

def monitorigisp_detail(request, pk):
    return HttpResponse(f'Судебный участок {pk}') 