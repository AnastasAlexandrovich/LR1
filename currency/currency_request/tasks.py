import datetime
import json
from datetime import timedelta

from celery.task import periodic_task
from fixerio import Fixerio

from .models import CurrencyModel


@periodic_task(run_every=(timedelta(hours=4)), name='update database')
def delete_not_confirmed_exchanges():
    fxrio = Fixerio(access_key='e09a7f016b0fd315c52e03a3d5cea36f')
    res = fxrio.latest()

    rates = res['rates']

    for key in rates.keys():
        CurrencyModel.objects.create(
            name=key,
            value=rates[key],
            timestamp=res['timestamp'],
            date=datetime.datetime.strptime(res['date'], "%Y-%m-%d").date()
        ).save()

    print('hey')

