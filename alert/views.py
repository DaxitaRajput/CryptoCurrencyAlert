'''This file is controller file '''
# import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, View
import crypto_compare
from .models import *
# from vanilla import CreateView, DeleteView, ListView, UpdateView, FormView, DetailView, RedirectView, View, TemplateView
from .forms import *
# Create your views here.


"""
This class is storing data in database pricealert table
"""
class PriceAlertDetails(FormView):
    template_name = 'alert/main_page.html'
    form_class = PriceAlertForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.POST.get('from_coin_type'):
            initial_coin_type = CryptoPriceAlert.objects.get(id=request.POST.get('from_coin_type')).from_coin_type
        if request.POST.get('above_coin_type'):
            above_price_coin_type = CryptoPriceAlert.objects.get(id=request.POST.get('above_coin_type')).from_coin_type
        if request.POST.get('below_coin_type'):
            below_price_coin_type = CryptoPriceAlert.objects.get(id=request.POST.get('below_coin_type')).from_coin_type
        above_price = request.POST.get('above_price')
        below_price = request.POST.get('below_price')
        email_id = request.POST.get('email_id')  
        data = {"json_type":"price_alert", "json_from_coin_type":initial_coin_type, "json_above_price":above_price, "json_above_coin_type":above_price_coin_type, "json_below_price":below_price, "json_below_coin_type":below_price_coin_type, "json_email_id":email_id}
        print(initial_coin_type, "  ", request.POST.get('above_price'), "  ", above_price_coin_type, "  ", request.POST.get('below_price'), "  ", below_price_coin_type, "  ", request.POST.get('email_id'))
        user = UserTable.objects.get_or_create(email_id=request.POST.get('email_id'))
        # import code; code.interact(local=dict(globals(), **locals()))
        u_p = UserPreference.objects.create(userid=user[0], json_data=data)
        print("added from price alert", u_p)
        # to get data from this json_data use this
        # import ast
        # ast.literal_eval(UserPreference.objects.filter(userid=UserTable.objects.get(email_id="email@gmail.com"))[3].json_data)['json_above_price']
        # UserPreference.objects.create(userid=user[0],json_data='{}')
        # return HttpResponseRedirect(reverse_lazy('price-alert'))
        return HttpResponseRedirect(reverse_lazy('main-page'))

""" this class stores data in volumealert table """
class VolumeAlertDetails(FormView):
    template_name = 'alert/main_page.html'
    form_class = VolumeAlertForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.POST.get('from_coin_type'):
            initial_coin_type = CryptoVolumePrice.objects.get(id=request.POST.get('from_coin_type')).from_coin_type
        if request.POST.get('above_coin_type'):
            above_volume_coin_type = CryptoVolumePrice.objects.get(id=request.POST.get('above_coin_type')).from_coin_type
        if request.POST.get('below_coin_type'):
            below_volume_coin_type = CryptoVolumePrice.objects.get(id=request.POST.get('below_coin_type')).from_coin_type
        above_volume = request.POST.get('above_volume')
        below_volume = request.POST.get('below_volume')
        email_id = request.POST.get('email_id')
            
        data = {"json_type":"volume_alert", "json_from_coin_type":initial_coin_type, "json_above_volume":above_volume, "json_above_coin_type":above_volume_coin_type, "json_below_volume":below_volume, "json_below_coin_type":below_volume_coin_type, "json_email_id":email_id}
        print(initial_coin_type, "  ", above_volume, "  ", above_volume_coin_type, "  ", below_volume, "  ", below_volume_coin_type, "  ", request.POST.get('email_id'))
        user = UserTable.objects.get_or_create(email_id=request.POST.get('email_id'))
        # import code; code.interact(local=dict(globals(), **locals()))
        u_p = UserPreference.objects.create(userid=user[0], json_data=data)
        print("added from volume alert", u_p)
        # to get data from this json_data use this
        # import ast
        # ast.literal_eval(UserPreference.objects.filter(userid=UserTable.objects.get(email_id="email@gmail.com"))[3].json_data)['json_above_price']
        # UserPreference.objects.create(userid=user[0], json_data='{}')
        # return HttpResponseRedirect(reverse_lazy('volume-alert'))
        return HttpResponseRedirect(reverse_lazy('main-page'))

""" this class stores data in marketcapalert table """
class MarketCapAlertDetails(FormView):
    template_name = 'alert/main_page.html'
    form_class = MarketCapAlertForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.POST.get('from_coin_type'):
            initial_coin_type = CryptoMarketCap.objects.get(id=request.POST.get('from_coin_type')).from_coin_type
        if request.POST.get('above_coin_type'):
            above_marketcap_coin_type = CryptoMarketCap.objects.get(id=request.POST.get('above_coin_type')).from_coin_type
        if request.POST.get('below_coin_type'):
            below_marketcap_coin_type = CryptoMarketCap.objects.get(id=request.POST.get('below_coin_type')).from_coin_type
        above_marketcap = request.POST.get('above_marketcap')
        below_marketcap = request.POST.get('below_marketcap')
        email_id = request.POST.get('email_id')
            
        data = {"json_type":"marketcap_alert", "json_from_coin_type":initial_coin_type, "json_above_marketcap":above_marketcap, "json_above_coin_type":above_marketcap_coin_type, "json_below_marketcap":below_marketcap, "json_below_coin_type":below_marketcap_coin_type, "json_email_id":email_id}
        print(initial_coin_type, "  ", above_marketcap, "  ", above_marketcap_coin_type, "  ", below_marketcap, "  ", below_marketcap_coin_type, "  ", request.POST.get('email_id'))
        user = UserTable.objects.get_or_create(email_id=request.POST.get('email_id'))
        # import code; code.interact(local=dict(globals(), **locals()))
        u_p = UserPreference.objects.create(userid=user[0], json_data=data)
        print("added from marketcap alert", u_p)
        # to get data from this json_data use this
        # import ast
        # ast.literal_eval(UserPreference.objects.filter(userid=UserTable.objects.get(email_id="email@gmail.com"))[3].json_data)['json_above_price']
        # UserPreference.objects.create(userid=user[0],json_data='{}')
        # return HttpResponseRedirect(reverse_lazy('marketcap-alert'))
        return HttpResponseRedirect(reverse_lazy('main-page'))

""" this class stores data in profitlossalert table """
class ProfitlossAlertDetails(FormView):
    template_name = 'alert/main_page.html'
    form_class = ProfitlossAlertForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(None)
        # import code; code.interact(local=dict(globals(), **locals()))
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.POST.get('from_coin_type'):
            initial_coin_type = CryptoPriceAlert.objects.get(id=request.POST.get('from_coin_type')).from_coin_type
        if request.POST.get('purchasing_coin_type'):
            purchasing_coin_type = CryptoPriceAlert.objects.get(id=request.POST.get('purchasing_coin_type')).from_coin_type
        # if request.POST.get('frequency'):
        #   below_marketcap_coin_type = CryptoPriceAlert.objects.get(id=request.POST.get('below_coin_type')).from_coin_type
        frequency = request.POST.get('frequency')
        purchasing_price = request.POST.get('purchasing_price')
        purchasing_quantity = request.POST.get('purchasing_quantity')
        email_id = request.POST.get('email_id')
            
        data = {"json_type":"profitloss_alert", "json_from_coin_type":initial_coin_type, "json_purchasing_price":purchasing_price, "json_purchasing_coin_type":purchasing_coin_type, "json_purchasing_quantity":purchasing_quantity, "json_frequency":frequency, "json_email_id":email_id}
        print(initial_coin_type, "  ", purchasing_price, "  ", purchasing_coin_type, "  ", purchasing_quantity, "  ", frequency, "  ", request.POST.get('email_id')) 
        user = UserTable.objects.get_or_create(email_id=request.POST.get('email_id'))
        # import code; code.interact(local=dict(globals(), **locals()))
        u_p = UserPreference.objects.create(userid=user[0], json_data=data)
        print("added from profitloss alert", u_p)
        # to get data from this json_data use this
        # import ast
        # ast.literal_eval(UserPreference.objects.filter(userid=UserTable.objects.get(email_id="email@gmail.com"))[3].json_data)['json_above_price']
        # UserPreference.objects.create(userid=user[0],json_data='{}')
        # return HttpResponseRedirect(reverse_lazy('marketcap-alert'))
        return HttpResponseRedirect(reverse_lazy('main-page'))

""" this class stores data in pricepercentagealert table """
class PricePercentageAlertDetails(FormView):
    template_name = 'alert/main_page.html'
    form_class = PricepercentageAlertForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.POST.get('from_coin_type'):
            initial_coin_type = CryptoPriceAlert.objects.get(id=request.POST.get('from_coin_type')).from_coin_type
        if request.POST.get('above_coin_type'):
            above_marketcap_coin_type = CryptoPriceAlert.objects.get(id=request.POST.get('above_coin_type')).from_coin_type
        if request.POST.get('below_coin_type'):
            below_marketcap_coin_type = CryptoPriceAlert.objects.get(id=request.POST.get('below_coin_type')).from_coin_type
        above_marketcap = request.POST.get('above_price_percentage')
        below_marketcap = request.POST.get('below_price_percentage')
        email_id = request.POST.get('email_id')
            
        data = {"json_type":"pricepercentage_alert", "json_from_coin_type":initial_coin_type, "json_above_marketcap":above_marketcap, "json_above_coin_type":above_marketcap_coin_type, "json_below_marketcap":below_marketcap, "json_below_coin_type":below_marketcap_coin_type, "json_email_id":email_id}
        print(initial_coin_type, "  ", above_marketcap, "  ", above_marketcap_coin_type, "  ", below_marketcap, "  ", below_marketcap_coin_type, "  ", request.POST.get('email_id'))
        
        user = UserTable.objects.get_or_create(email_id=request.POST.get('email_id'))
        # import code; code.interact(local=dict(globals(), **locals()))
        u_p = UserPreference.objects.create(userid=user[0], json_data=data)
        print("added from price percentage alert", u_p)
        # to get data from this json_data use this
        # import ast
        # ast.literal_eval(UserPreference.objects.filter(userid=UserTable.objects.get(email_id="email@gmail.com"))[3].json_data)['json_above_price']
        # UserPreference.objects.create(userid=user[0],json_data='{}')
        # return HttpResponseRedirect(reverse_lazy('pricepercentage-alert'))
        return HttpResponseRedirect(reverse_lazy('main-page'))

""" 
this class sends forms in main page 
"""
class IndexView(View):
    template_name = 'alert/main_page.html'
    form_classes = {'price': PriceAlertForm, 
                    'volume': VolumeAlertForm, 
                    'marketcap':MarketCapAlertForm,
                    'profitloss':ProfitlossAlertForm,
                    'pricepercentage':PricepercentageAlertForm}
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'forms':self.form_classes})

""" this is for developer r&d """
def index(request):
    
    crypto_compare_client = crypto_compare.Client() #Create an instance and call any public API method!
    import code; code.interact(local=dict(globals(), **locals()))
    # crypto_compare_client.coin_list()
    # btc_coin_id = crypto_compare_client.coin_list()['Data']['BTC']['Id']
    # import code; code.interact(local=dict(globals(),**locals()))
    # print("snapshot=",crypto_compare_client.coin_snapshot('BTC', 'USD'))
    # print(crypto_compare_client.coin_snapshot_full_by_id(btc_coin_id))
    # import code; code.interact(local=dict(globals(), **locals()))
    # for find current value of coin JPY and EUR in BTC coin
    
    # a_1 = 'BTC'
    # b_2 = 'ETH'
    # prices = crypto_compare_client.price(fsym=a, tsyms=b)
    # data = crypto_compare_client.price_multifull(fsyms=a, tsyms=b)
    # for coin in b.split(','):
    #CryptoPriceAlert.objects.create(from_coin_type=a,to_coin_type=coin,current_price=prices[coin],previous_price=prices[coin])
    #   CryptoVolumePrice.objects.create(from_coin_type=a,to_coin_type=coin,current_volume=data['DISPLAY'][a][coin]['VOLUMEDAY'],previous_volume=data['DISPLAY'][a][coin]['VOLUMEDAY'])
    #   CryptoMarketCap.objects.create(from_coin_type=a,to_coin_type=coin,current_marketcap=data['DISPLAY'][a][coin]['MKTCAP'],previous_marketcap=data['DISPLAY'][a][coin]['MKTCAP'])
    print("data created")

    # UserPreference.objects.create(userid=UserTable.objects.get(id=2),json_data='{"coin_type":"BTC","above_price":239,"above_price_coin_type":"USD","below_price":200,"below_price_coin_type":"USD"}')
    u_ps = UserPreference.objects.filter(userid=UserTable.objects.get(id=2))
    # json.loads(u_ps[1].json_data)['coin_type']

    # import code; code.interact(local=dict(globals(), **locals()))
    
    # print("price of jpy and eur =",crypto_compare_client.price(fsym='ETH',tsyms='BTC,USD'))
    # print("multi price=",crypto_compare_client.price_multi(fsyms='ETH,BTC',tsyms='USD,EUR,ETH'))
    # print("price multifull=",crypto_compare_client.price_multifull(fsyms='ETH,BTC',tsyms='USD,EUR,ETH'))

    # print("Top volumn of btc is : ",crypto_compare_client.top_volumes(tsym='BTC'))
    # print("avg = ",crypto_compare_client.generate_avg(fsym='ETH',tsym='BTC',e='coinbase',markets='BTC'))
    # import code; code.interact(local=dict(globals(), **locals()))
    return HttpResponse(request,"return this string")




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
#   print(value['Symbol'])

# select up.userid_id,pa.current_price from alert_userpreference as up,alert_cryptopricealert as pa where CAST(pa.current_price as FLOAT) <20 and CAST(pa.current_price as FLOAT)>10;
