
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('',views.http_response,name='home'),
    path('lnk/<str:short_url>/',views.get_url,name='get_url'),
    path('add/',views.add_url,name='add_url'),
    



]
