from django.db import models

# Create your models here.




# Create your models here.
class url_table(models.Model):
    raw_url= models.CharField(max_length=300)
    short_url= models.CharField(max_length=7)






