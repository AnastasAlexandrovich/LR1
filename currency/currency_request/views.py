import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from fixerio import Fixerio

from .models import CurrencyModel


class ExchangeCurrencyView(View):
    def post(self, request):
        req_json = json.loads(request.body)
        cur_from = req_json['from']
        cur_to = req_json['to']
        fxrio = Fixerio(access_key='e09a7f016b0fd315c52e03a3d5cea36f')
        cur_res = fxrio.latest(symbols=[cur_from, cur_to])
        res = cur_res['rates'][cur_to] / cur_res['rates'][cur_from]
        return HttpResponse(res)

    def get(self, request):
        currencies = CurrencyModel.objects.all()
        responses = []
        for currency in currencies:
            responses.append(
                {
                    'id': currency.id,
                    'name': currency.name,
                    'value': currency.value,
                    'timestamp': currency.timestamp,
                    'date': str(currency.date)
                }
            )
        return HttpResponse(json.dumps(responses), status=200, content_type="application/json")

