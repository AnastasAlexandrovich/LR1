from django.db import models


class CurrencyModel(models.Model):
    name = models.CharField(verbose_name="Валюта", blank=False, null=False, max_length=3)
    value = models.FloatField(verbose_name="Стоимость", blank=False, null=False)
    timestamp = models.BigIntegerField(verbose_name="Временная метка", blank=False, null=False)
    date = models.DateField(verbose_name="Дата", blank=False, null=False)
