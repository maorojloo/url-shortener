
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.http_response),
    path('lnk/<str:short_url>/',views.get_url,name='get_url'),



]
