from django import forms
from django.db import models
from django.forms import fields
from . import models

class adding_url_form(forms.ModelForm):
    

    class Meta:
        model=models.url_table
        fields=['raw_url','exp_time']



    

