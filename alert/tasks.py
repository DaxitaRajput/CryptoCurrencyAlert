from celery.task.schedules import crontab
from celery.decorators import periodic_task,task
from celery.utils.log import get_task_logger
from django.conf import settings
from celery import shared_task
from .models import *
import os
import sys
import subprocess
import pathlib
from django.utils import timezone
import crypto_compare


@task(name="test", ignore_result=True)
def save_cc_api_data(param):
	coin_list = []
	price_alert_dict = {}
	volume_alert_dict = {}
	crypto_compare_client = crypto_compare.Client()
	coins = crypto_compare_client.coin_list()
	for key,value in coins['Data'].items():
		coin_list.append(value['Symbol'])

	to_coins = 'BTC,USD,AUD,BGN,BRL,CAD,CHF,CNY,CZK,DKK,EUR,GBP,HKD,HRK,HUF,IDR,ILS,INR,ISK,JPY,KRW,MXN,MYR,NOK,NZD,PHP,PLN,RON,RUB,SEK,SGD,THB,TRY,ZAR'

	for coin in coin_list:
		try:
			price_alert_dict.update({coin:crypto_compare_client.price(fsym=coin, tsyms=to_coins)})
		except:
			pass

	for key,j in price_alert_dict.items():
		for k,value in j.items():
			print("for ",key," value of ",k," is ",value)


	# CryptoPriceAlert.objects.create(from_coin_type)



	to_coins_vol1 = 'BTC,USD,AUD,BGN,BRL,CAD,CHF,CNY,CZK,DKK,EUR,GBP,HKD,HRK,HUF,IDR,ILS,INR'
	to_coins_vol2 = 'ISK,JPY,KRW,MXN,MYR,NOK,NZD,PHP,PLN,RON,RUB,SEK,SGD,THB,TRY,ZAR'

	for coin in coin_list:
		try:
			a = crypto_compare_client.price_multifull(fsyms=coin,tsyms=to_coins_vol1)
			b = crypto_compare_client.price_multifull(fsyms=coin,tsyms=to_coins_vol2)
			a['DISPLAY'][c]['USD']['VOLUMEDAY']


    return 'The test task executed with argument "%s" ' % param

@task(name="add_entry", ignore_result=True)
def check_rules_and_send_email(task):
	print("in save cc")

@task(name="sum_two_numbers")
def add(x, y):
	return x + y

@task(name="multiply_two_numbers")
def mul(x, y):
	return x * y
