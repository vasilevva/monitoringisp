from ast import Not, Return

import fdb
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import UpdateMonitoringForm
from .models import DbAmirs, MonitoringIsp


def get_monitoringisp_data(host, port, path, user, password, sql_dialect, charset):
    try:
        con = fdb.connect(
            host=host,
            port=port,
            database=path,
            user=user,
            password=password,
            sql_dialect=sql_dialect,
            charset=charset
        )
        try:
            cur = con.cursor()
            cur.execute('''
                SELECT COUNT(DISTINCT "ExternalQuery")
                FROM "ExternalSystemLogRecord" 
                WHERE "LogMessage" 
                LIKE 'Создана квитанция о подтверждении приема сообщения%';
            ''')
            receiveddoc = cur.fetchall()[0][0]
            cur.execute('''
                SELECT COUNT("OID") 
                FROM "ExternalSystemLogRecord" 
                WHERE "LogMessage" 
                LIKE '%Постановление о возбуждении исполнительного производства%';
            ''')
            opencase=cur.fetchall()[0][0]
        except Exception as error:
            print(error) 
            return None
        finally:
            con.close()
    except Exception as error:
        print(error) 
        return None
    return {'receiveddoc': receiveddoc, 'opencase': opencase}


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
        'page_obj': page_obj.order_by('nomeruch'),
        'listuch': listuch,
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        objuch = form.cleaned_data['nomeruch']
        obj_dbamirs = get_object_or_404(DbAmirs, nomeruch=objuch)
        monitoringdata = get_monitoringisp_data(
            host=getattr(obj_dbamirs.server, 'ip'),
            port=obj_dbamirs.port,
            path=obj_dbamirs.pathtodb,
            user=obj_dbamirs.login,
            password=obj_dbamirs.password,
            sql_dialect=obj_dbamirs.sql_dialect,
            charset=obj_dbamirs.charset
        )
        if monitoringdata is not None:
            MonitoringIsp.objects.create(
                receiveddoc=monitoringdata['receiveddoc'],
                opencase=monitoringdata['opencase'],
                nomeruch=objuch
            )
            '''
            MonitoringIsp.objects.create(
                receiveddoc=0,
                opencase=0,
                nomeruch=objuch
            )
            '''
        return redirect('monitoring_isp:monitorig_isp')
        
    return render(request, 'monitoring_isp/monitorigisp.html', context)

def monitorigisp_detail(request, pk):
    return HttpResponse(f'Судебный участок {pk}')
