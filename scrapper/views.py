# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Influxdb.Db import InfluxDBInstance
from django.conf import settings

from utils import web_dict

# Create your views here.

def currency_list_view(request):
    new_db_instance = InfluxDBInstance(
        settings.INFLUXDB_DATABASE,
        settings.INFLUXDB_USER,
        settings.INFLUXDB_PASSWORD,
        settings.INFLUXDB_HOST,
        settings.INFLUXDB_PORT
    )
    db_data = new_db_instance.query_data("SHOW MEASUREMENTS;")
    return render(
        request,
        'currency_list_view.html',
        {'data': db_data.raw["series"][0]["values"]}
    )

def currency_data_view(request, currency):
    new_db_instance = InfluxDBInstance(
        settings.INFLUXDB_DATABASE,
        settings.INFLUXDB_USER,
        settings.INFLUXDB_PASSWORD,
        settings.INFLUXDB_HOST,
        settings.INFLUXDB_PORT
    )
    db_data = new_db_instance.query_data("SELECT * FROM " + currency + ";")
    return render(
        request,
        'currency_data_view.html',
        {
            'data': db_data.raw["series"][0]["values"],
            'currency': currency
        }
    )

def currency_now_view(request, currency):
    get_data = web_dict("https://blockchain.info/ticker")
    if get_data[currency]:
        return render(
            request,
            'currency_now_view.html',
            {
                'data': get_data[currency],
                'currency': currency
            }
        )
    else:
        return render(
            request,
            'currency_now_view.html',
            {'currency': currency}
        )
