from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import UpdateMonitoringForm
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
    form = UpdateMonitoringForm(request.POST or None)
    context = {
        'page_obj': page_obj,
        'listuch': listuch,
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        print(form.cleaned_data)
        print('!!!!!!!!!!!!!!!!!!!!!')
    return render(request, 'monitoring_isp/monitorigisp.html', context)

def monitorigisp_detail(request, pk):
    return HttpResponse(f'Судебный участок {pk}') 
