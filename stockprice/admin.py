from django.contrib import admin
from .models import CompanyList
from .models import HistoricalData

# Register your models here.

admin.site.register(CompanyList)
admin.site.register(HistoricalData)
