import time

from celery import shared_task

from performance.models import DailyPerformance

@shared_task()
def slow_iteration_task():
    daily_perfs = DailyPerformance.objects.all()[:50]

    index = 1
    for daily_perf in daily_perfs:
        print("{}: {}".format(index, daily_perf.profit))
        time.sleep(60)
        
        index += 1
