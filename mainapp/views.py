from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.db import connection
from django.shortcuts import redirect

# Create your views here.

def http_response(request):
    return HttpResponse('<h1>Hello :)</h1>')    

def get_url(request,short_url):
    q=""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mainapp_url_table WHERE short_url = '1'")
    row = cursor.fetchone()
    raw_url=row[1]
    response = redirect(row[1])
    return response



    
    return HttpResponse(short_url)