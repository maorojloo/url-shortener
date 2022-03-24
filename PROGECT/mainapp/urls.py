
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


app_name = 'mainapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('lnk/<str:short_url>/',views.get_url,name='get_url'),
    path('add/',views.add_url,name='add_url'),
    path('myurls/',views.show_urls,name='myurls'),
    path('api/chart/<int:pk>', views.chart_data.as_view(), name='api-chart-data'),
    path('chart/<int:pk>',views.chart,name='chart'),

    



]
