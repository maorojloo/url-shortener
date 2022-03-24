from cProfile import label
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.db import connection
from django.shortcuts import redirect
from . import forms
from django.contrib import messages
from .forms import adding_url_form
import json
import string  
import re
import secrets 
from django.contrib.auth.decorators import login_required
import ast
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from datetime import date, timedelta


# Create your views here.

def url_shortner(raw_lnk):
    # import package  
    num = 10 # define the length of the string  
    # define the secrets.choice() method and pass the string.ascii_letters + string.digits as an parameters.  
    res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
    return str(res)



def home(request):
    return render(request,'mainapp/home.html')    
 
def visit_saver(id):
    print("visit save")
    obj = models.url_table.objects.get(pk=id)
    obj.visitor_count = obj.visitor_count+1
    
    convertedDict = ast.literal_eval(obj.visit_day)
    current_time=datetime.today().strftime('%Y-%m-%d')
    if current_time in convertedDict:
        x_count=convertedDict.get(current_time)
        x_count=x_count+1
        convertedDict.update({current_time: x_count}) 
    else:
        convertedDict.update({current_time: 1}) 
        
    



    obj.visit_day=convertedDict    
 
    obj.save()



def get_url(request,short_url): 
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mainapp_url_table WHERE short_url = '"+short_url+"'")
    row = cursor.fetchone()
    raw_url=row[1]
    pk=row[0]
    print(pk)
    visit_saver(pk)
    redirect_url="http://"+raw_url
    
    response = redirect(redirect_url)
    return response



@login_required(login_url='/login/') #redirect when user is not logged in
def add_url(request):
    add_template_name='mainapp/add_url.html'
    redirect_url='home'
    form = adding_url_form(request.POST or None)
    if form.is_valid():
        data=form.save(commit=False)
        
        form = forms.adding_url_form(request.POST or None)        
        data.owner = request.user.username
        data.visit_day='{}'
        
        x = re.findall("^http://(.*)|^https://(.*)", data.raw_url)
        if x:
            x=x[0]
        if x[0]=="":
            data.raw_url=x[1]
        if x[1]=="":
            data.raw_url=x[0]

        else:
            pass

        data.short_url=url_shortner(data.raw_url)
        data.save()
        messages.success(request,"item has been added successfully "+"127.0.0.1:8000/lnk/"+data.short_url)
        visit_saver(data.id)
        return redirect('mainapp:home')
    else:
        print('else')
        if request.method =='POST':
            messages.warning(request, 'some things went wrong try again')
        print(form)
        return render (request, add_template_name ,{'form':form} )



def show_urls(request):
    urls = models.url_table.objects.all().filter(owner=request.user.username)
    return render(request,'mainapp/myurls.html',{'urls':urls})
    
    

# Creating views
def api_data(TemplateView):
    return JsonResponse(data = {'a': 10,'b': 20,})

def chart(request,pk):
    return render(request,'mainapp/data_visulising.html',{"pk":pk})    

class chart_data(APIView):

    authentication_classes = []
    permission_classes = []

    
    def get(self,request, format=None,pk=None):
        obj = models.url_table.objects.get(id=pk)
        str=obj.visit_day
        str = str.replace("\'", "\"")
        visit_day_dict = json.loads(str)


        labels=list(visit_day_dict.keys())
        datas=list(visit_day_dict.values())
        print(obj.creation_time.date())

"""


    

        from datetime import date, timedelta,datetime
        
        
        #x = re.findall("^http://(.*)|^https://(.*)", data.raw_url)
        
        sdate = date(2008, 8, 15)   # start date
        edate = datetime.date(datetime.now())   # end date

        delta = edate - sdate       # as timedelta

        for i in range(delta.days + 1):
            day = sdate + timedelta(days=i)
            print(day)


"""





        return Response({'l':labels,'d':datas}) 



    
    