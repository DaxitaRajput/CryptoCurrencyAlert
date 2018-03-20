from django.shortcuts import render
from django.http import HttpResponse
import crypto_compare
import json
from .models import *
# Create your views here.
def index(request):
	
	crypto_compare_client = crypto_compare.Client() #Create an instance and call any public API method!
	# import code; code.interact(local=dict(globals(), **locals()))
	# crypto_compare_client.coin_list()
	# btc_coin_id = crypto_compare_client.coin_list()['Data']['BTC']['Id']
	# import code; code.interact(local=dict(globals(), **locals()))
	# print("snapshot=",crypto_compare_client.coin_snapshot('BTC', 'USD'))
	# print(crypto_compare_client.coin_snapshot_full_by_id(btc_coin_id))
	# import code; code.interact(local=dict(globals(), **locals()))
	# for find current value of coin JPY and EUR in BTC coin
	
	a='BTC'
	b='ETH'
	prices = crypto_compare_client.price(fsym=a,tsyms=b)
	data = crypto_compare_client.price_multifull(fsyms=a,tsyms=b)
	# for coin in b.split(','):
	# 	CryptoPriceAlert.objects.create(from_coin_type=a,to_coin_type=coin,current_price=prices[coin],previous_price=prices[coin])
	# 	CryptoVolumePrice.objects.create(from_coin_type=a,to_coin_type=coin,current_volume=data['DISPLAY'][a][coin]['VOLUMEDAY'],previous_volume=data['DISPLAY'][a][coin]['VOLUMEDAY'])
	# 	CryptoMarketCap.objects.create(from_coin_type=a,to_coin_type=coin,current_marketcap=data['DISPLAY'][a][coin]['MKTCAP'],previous_marketcap=data['DISPLAY'][a][coin]['MKTCAP'])
	print("data created")

	# UserPreference.objects.create(userid=UserTable.objects.get(id=2),json_data='{"coin_type":"BTC","above_price":239,"above_price_coin_type":"USD","below_price":200,"below_price_coin_type":"USD"}')
	u_ps=UserPreference.objects.filter(userid=UserTable.objects.get(id=2))
	json.loads(u_ps[1].json_data)['coin_type']

	import code; code.interact(local=dict(globals(), **locals()))
	
	# print("price of jpy and eur =",crypto_compare_client.price(fsym='ETH',tsyms='BTC,USD'))
	# print("multi price=",crypto_compare_client.price_multi(fsyms='ETH,BTC',tsyms='USD,EUR,ETH'))
	# print("price multifull=",crypto_compare_client.price_multifull(fsyms='ETH,BTC',tsyms='USD,EUR,ETH'))

	# print("Top volumn of btc is : ",crypto_compare_client.top_volumes(tsym='BTC'))
	# print("avg = ",crypto_compare_client.generate_avg(fsym='ETH',tsym='BTC',e='coinbase',markets='BTC'))
	# import code; code.interact(local=dict(globals(), **locals()))
	return HttpResponse("return this string")




####################################################
# get price of last of 24 hr
# a= crypto_compare_client.price_multifull(fsyms='ETH,BTC',tsyms='USD')
# a['DISPLAY']['ETH']['USD']['CHANGEPCT24HOUR']
# # get volume of 24 hr
# a['DISPLAY']['ETH']['USD']['VOLUME24HOUR']
# a['DISPLAY']['ETH']['USD']


# {LASTMARKET': 'Gemini', 'MKTCAP': '$ 59.76 B', 'TOTALVOLUME24HTO': '$ 754.06 M', 'OPENDAY': '$ 610.56', 'FROMSYMBOL': 'Ξ', 'HIGH24HOUR': '$ 621.65', 'CHANGEDAY': '$ -2.09', 'LASTUPDATE': 'Just now', 'LOW24HOUR': '$ 583.38', 'PRICE': '$ 608.47', 'MARKET': 'CryptoCompare Index', 'CHANGE24HOUR': '$ 22.25', 'SUPPLY': 'Ξ 98,216,999.8', 'CHANGEPCTDAY': '-0.34', 'OPEN24HOUR': '$ 586.22', 'LASTVOLUME': 'Ξ 0.03705', 'VOLUMEDAY': 'Ξ 104,104.4', 'TOSYMBOL': '$', 'CHANGEPCT24HOUR': '3.80', 'LASTVOLUMETO': '$ 22.54', 'VOLUME24HOUR': 'Ξ 441,262.9', 'LOWDAY': '$ 585.16', 'VOLUME24HOURTO': '$ 266,717,479.1', 'HIGHDAY': '$ 615.03', 'LASTTRADEID': '3282315943', 'VOLUMEDAYTO': '$ 62,465,314.1', 'TOTALVOLUME24H': 'Ξ 1,242.20 K'}

# a['DISPLAY']['ETH']['USD']['CHANGE24HOUR']

# get current volume
# a['DISPLAY']['ETH']['USD']['VOLUMEDAY']

# for find current value of coin JPY and EUR in BTC coin
# print("price of jpy and eur =",crypto_compare_client.price(fsym='ETH',tsyms='BTC,USD'))


# get the market cap value
# a['DISPLAY']['BTC']['USD']['MKTCAP']



# get coin list
# coin_list=crypto_compare_client.coin_list()
# for key,value in coin_list['Data'].items():
# 	print(value['Symbol'])

# select up.userid_id,pa.current_price from alert_userpreference as up,alert_cryptopricealert as pa where CAST(pa.current_price as FLOAT) <20 and CAST(pa.current_price as FLOAT)>10;