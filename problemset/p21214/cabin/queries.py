from django.db.models import Sum, F, Value, Q, Count
from django.db.models.lookups import GreaterThan, GreaterThanOrEqual

from cabin.models import *


def query_0(x):
    q = Driver.objects.filter(rating__gt=x)
    return q


def query_1(x):
    q = Payment.objects.filter(ride__car__owner=x).aggregate(payment_sum=Sum('amount', default=None))
    return q


def query_2(x):
    q = Ride.objects.filter(request__rider=x).select_related('request')
    return q


def query_3(t):
    q = Ride.objects.annotate(duration=F('dropoff_time')-F('pickup_time')).filter(duration__gt=t).count()
    return q


def query_4(x, y, r):
    q = Driver.objects.filter(active=True).filter(GreaterThan(Value(r**2), ((F('x')-Value(x)) ** 2) + ((F('y')-Value(y)) ** 2)))
    return q


def query_5(n, c):
    q = Driver.objects.filter(
        Q(car__car_type='A') | Q(car__color=c)
    ).annotate(
        num_rides=Count('car__ride')
    ).filter(
        num_rides__gte=n
    )
    return q


def query_6(x, t):
    q = Rider.objects.annotate(
        num_rides=Count('riderequest__ride')
    ).filter(
        num_rides__gte=x
    ).annotate(
        sum_paid=Sum('riderequest__ride__payment__amount', default=0)
    ).filter(
        sum_paid__gte=t
    )
    return q


def query_7():
    q = Ride.objects.filter(
        car__owner__account__first_name=F('request__rider__account__first_name')
    )
    print(q)
    return q


def query_8():
    q = 'your query here'
    return q


def query_9(n, t):
    q = 'your query here'
    return q


def query_10():
    q = 'your query here'
    return q
