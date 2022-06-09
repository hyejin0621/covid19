from django.db import models

# Create your models here.
class CovidData(models.Model):
    co_data = models.CharField(max_length = 50)

class CovidPer(models.Model):
    co_per = models.CharField(max_length = 50)

class DailyCovid(models.Model):
    date1 = models.CharField(max_length = 50)
    da_co = models.CharField(max_length = 50)