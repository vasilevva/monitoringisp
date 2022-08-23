from django.urls import path

from . import views

app_name = 'monitorig_isp'

urlpatterns = [
    
    path('', views.monitorigisp, name='monitorig_isp'),
    path('<int:pk>/', views.monitorigisp_detail, name='monitorigisp_detail'),
] 
