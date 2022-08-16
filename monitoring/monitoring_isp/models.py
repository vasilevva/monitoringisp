from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model() 

class Uch(models.Model):
    numer = models.PositiveSmallIntegerField()
    
class Server(models.Model):
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    dnsname = models.CharField(max_length=30)

class DbAmirs(models.Model):
    ipserver = models.ForeignKey(Server, verbose_name='IP',
                               related_name='ip_dbamirs',
                               on_delete=models.CASCADE)
    servername = models.ForeignKey(Server, verbose_name='servername',
                               related_name='name_dbamirs',
                               on_delete=models.CASCADE)
    nomeruch = models.ForeignKey(Server, verbose_name='nomeruch',
                               related_name='uch_dbamirs',
                               on_delete=models.CASCADE)
    port = models.PositiveSmallIntegerField(default=3050)
    pathtodb = models.CharField(max_length=500)   
    receiveddoc = models.PositiveSmallIntegerField()
    opencase = models.PositiveSmallIntegerField()
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['nomeruch']

class MonitoringIsp(models.Model):
    receiveddoc = models.PositiveSmallIntegerField()
    received = models.PositiveSmallIntegerField()
    nomeruch = models.ForeignKey(Server, verbose_name='IP',
                               related_name='uch_isp',
                               on_delete=models.CASCADE)
    monitoringdata = models.DateTimeField('Добавлен', auto_now_add=True) 
