import random

from django.core.management.base import BaseCommand

from performance.models import DailyPerformance

class Command(BaseCommand):

    def handle(self, **options):
        daily_perfs = DailyPerformance.objects.filter_by_min_roi(0.5)
        total = len(daily_perfs)
        print("Length of perfs * 2 = ", total * 2)

        index = 1
        for daily_perf in daily_perfs:
            print("{}/{}".format(index, total))
            
            new_revenue = daily_perf.revenue * round(random.uniform(0.5, 2), 1)
            daily_perf.revenue = new_revenue
            daily_perf.save()
            
            index += 1
