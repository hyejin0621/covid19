from django.contrib import admin
from .models import CovidData
from .models import CovidPer
from .models import DailyCovid

# Register your models here.
admin.site.register(CovidData)
admin.site.register(CovidPer)
admin.site.register(DailyCovid)
