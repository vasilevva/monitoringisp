import fdb
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import UpdateMonitoringForm
from .models import DbAmirs, MonitoringIsp


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
        objuch = form.cleaned_data['nomeruch']
        obj_dbamirs = get_object_or_404(DbAmirs, nomeruch=objuch)
        host = getattr(obj_dbamirs.server, 'ip')
        path = obj_dbamirs.pathtodb
        port = obj_dbamirs.port
        user = obj_dbamirs.login
        password = obj_dbamirs.password
        sql_dialect = obj_dbamirs.sql_dialect
        charset = obj_dbamirs.charset
        print(host, path, port, user, password, sql_dialect, charset)
        con = fdb.connect(host=host,
                  port=port,
                  database=path,
                  user=user,
                  password=password,
                  sql_dialect=sql_dialect,
                  charset=charset)
        cur = con.cursor()
        cur.execute('''SELECT COUNT("OID") FROM "ExternalSystemLogRecord" WHERE "LogMessage" LIKE 'Создана квитанция о подтверждении%';''')
        receiveddoc = cur.fetchall()[0][0]

        MonitoringIsp.objects.create(receiveddoc = receiveddoc, opencase = 0,
                                    nomeruch =  objuch)
                
    return render(request, 'monitoring_isp/monitorigisp.html', context)

def monitorigisp_detail(request, pk):
    return HttpResponse(f'Судебный участок {pk}')
