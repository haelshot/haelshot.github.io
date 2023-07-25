# admin.py
from django.contrib import admin
from .models import CrimeData, Country, HomicideRate, HomicidePercentage

admin.site.register(CrimeData)
admin.site.register(Country)
admin.site.register(HomicideRate)
admin.site.register(HomicidePercentage)
