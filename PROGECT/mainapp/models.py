from statistics import mode
from django.db import models
from django.utils.timezone import now

# Create your models here.




# Create your models here.
class url_table(models.Model):
    raw_url= models.CharField(max_length=300)
    short_url= models.CharField(max_length=10)
    owner=models.CharField(max_length=30)
#pub_date = models.DateField(null=True, blank=True)
    exp_time=models.DateTimeField(null=True, blank=True)
    creation_time=models.DateTimeField(default=now)

    visitor_count=models.IntegerField(default=0)
    visit_day=models.CharField(default='{}',max_length=100000) 





    def __str__(self):
        return self.raw_url







