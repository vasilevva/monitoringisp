from django.urls import path

from . import views

app_name = 'monitorigisp'

urlpatterns = [
    
    path('', views.monitorigisp, name='monitorigisp_list'),
    path('<int:pk>/', views.monitorigisp_detail, name='monitorigisp_detail'),
] 