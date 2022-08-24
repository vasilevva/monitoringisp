from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model() 

class Uch(models.Model):
    numer = models.PositiveSmallIntegerField()
        
    def __str__(self) -> str:
        return f'Судебный участок {self.numer}'
    
    class Meta:
        ordering = ['numer']
    
class Server(models.Model):
    ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    dnsname = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f' {self.dnsname} ip: {self.ip}'

class DbAmirs(models.Model):
    server = models.ForeignKey(Server, verbose_name='server',
                               related_name='dbamirs',
                               on_delete=models.CASCADE)
    nomeruch = models.ForeignKey(Uch, verbose_name='nomeruch',
                               related_name='uch_dbamirs',
                               on_delete=models.CASCADE)
    port = models.PositiveSmallIntegerField(default=3050)
    pathtodb = models.CharField(max_length=500)   
    login = models.CharField(max_length=100, default='SYSDBA')
    password = models.CharField(max_length=100, default='masterkey')
    sql_dialect = models.PositiveSmallIntegerField(default=3)
    charset = models.CharField(max_length=100, default='WIN1251')
    
    class Meta:
        ordering = ['nomeruch']

class MonitoringIsp(models.Model):
    receiveddoc = models.PositiveSmallIntegerField()
    opencase = models.PositiveSmallIntegerField()
    nomeruch = models.ForeignKey(Uch, verbose_name='nomeruch',
                               related_name='MonitoringIsp',
                               on_delete=models.CASCADE)
    monitoringdata = models.DateTimeField('Добавлен', auto_now_add=True) 
