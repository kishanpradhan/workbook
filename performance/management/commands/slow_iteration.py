
from django.core.management.base import BaseCommand

from performance.models import DailyPerformance
from performance.tasks import slow_iteration_task

class Command(BaseCommand):
    
    def handle(self, **options):
        slow_iteration_task.delay()
        print("Slow iteration should be running in celery by now. Check celery worker log")
