from django.contrib import admin

from .models import DbAmirs, Server, Uch

# Register your models here.

class UchAdmin(admin.ModelAdmin):
    list_display = ('pk','numer',) 
    list_filter = ('numer',) 
    
admin.site.register(Uch, UchAdmin)

class ServerAdmin(admin.ModelAdmin):
    list_display = ('pk','ip', 'dnsname',) 
    search_fields = ('ip', 'dnsname',) 

admin.site.register(Server, ServerAdmin)

class DbAmirsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'server', 'nomeruch', 'port',
                    'pathtodb', 'login', 'password',
                    'sql_dialect', 'charset') 
    search_fields = ('nomeruch',) 

    list_filter = ('nomeruch',) 

admin.site.register(DbAmirs, DbAmirsAdmin)