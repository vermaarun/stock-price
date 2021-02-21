from django.db import models


# Create your models here.
class HistoricalData(models.Model):
    date = models.CharField(max_length=10)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adjClose = models.FloatField()
    volume = models.FloatField()
    unadjustedVolume = models.FloatField()
    change = models.FloatField()
    changePercent = models.FloatField()
    vwap = models.FloatField()
    label = models.CharField(max_length=10, default='')
    changeOverTime = models.FloatField()
    companyId = models.IntegerField()


class CompanyList(models.Model):
    name = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.name
