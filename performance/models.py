from statistics import mode
from django.db import models
from django.db.models import F
from django.utils.timezone import now
from django.db.models.functions import Cast


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    creation_date = models.DateTimeField(default=now, null=False)

class ROIManager(models.Manager):

    def filter_by_min_roi(self, min_roi: float):
        qs = self.annotate(roi=Cast(F("profit"), models.FloatField()) / Cast(F("cost"), models.FloatField()))
        return qs.filter(roi__gte=min_roi)

class Performance(BaseModel):
    cost = models.BigIntegerField(null=False)
    revenue = models.BigIntegerField(null=False)
    profit = models.BigIntegerField(null=False)

    objects = ROIManager()

    def get_profit(self):
        return self.revenue - self.cost
    
    def save(self, *args, **kwargs):
        self.profit = self.get_profit()
        super(Performance, self).save(*args, **kwargs)

class HourlyPerformance(Performance):
    datetime = models.DateTimeField(null=False)

class DailyPerformance(Performance):
    date = models.DateField(null=False)
