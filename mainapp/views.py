from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.db import connection
from django.shortcuts import redirect
from . import forms
from django.contrib import messages
from .forms import adding_url_form
import base64
import random   
import string  
import secrets 



# Create your views here.

def url_shortner(raw_lnk):
    # import package  
    num = 10 # define the length of the string  
    # define the secrets.choice() method and pass the string.ascii_letters + string.digits as an parameters.  
    res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
    return str(res)



def http_response(request):
    return HttpResponse('<h1>Hello :)</h1>')    
 
def get_url(request,short_url):
    q=""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mainapp_url_table WHERE short_url = '1'")
    row = cursor.fetchone()
    raw_url=row[1]
    response = redirect(raw_url)
    return response

def add_url(request):
    add_template_name='mainapp/add_url.html'
    redirect_url='home'
    form = adding_url_form(request.POST or None)
    if form.is_valid():
        data=form.save(commit=False)
        messages.success(request,"item has been added successfully")
        form = forms.adding_url_form(request.POST or None)        
        data.owner = request.user.username
        data.short_url=url_shortner(data.raw_url)
        data.save()
        return redirect('mainapp:home')
    else:
        print('else')
        if request.method =='POST':
            messages.warning(request, 'some things went wrong try again')
        print(form)
        return render (request, add_template_name ,{'form':form} )









    
    