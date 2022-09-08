import datetime
import pytest

from performance.models import DailyPerformance
from performance.management.commands import random_revenue, slow_iteration
from workbook.celery import app


@pytest.fixture
def create_daily_performance():
    DailyPerformance.objects.create(date=datetime.date(2022, 9, 6), cost=14, revenue=22)
    DailyPerformance.objects.create(date=datetime.date(2022, 9, 5), cost=13, revenue=20)
    DailyPerformance.objects.create(date=datetime.date(2022, 9, 6), cost=12, revenue=11)
    DailyPerformance.objects.create(date=datetime.date(2022, 9, 7), cost=12, revenue=14)

@pytest.fixture
def celery_app(request):
    app.conf.update(CELERY_ALWAYS_EAGER=True)
    return app


@pytest.mark.django_db
def test_random_revenue(capfd, create_daily_performance):

    random_revenue.Command().handle()
    out, err = capfd.readouterr()
    assert err == ""
    assert out == "Length of perfs * 2 =  4\n1/2\n2/2\n"


@pytest.mark.django_db
def test_slow_iteration(capfd, create_daily_performance, celery_app):

    slow_iteration.Command().handle()
    out, err = capfd.readouterr()
    assert err == ""
    assert out == "1: 8\n2: 7\n3: -1\n4: 2\nSlow iteration should be running in celery by now. Check celery worker log\n"
