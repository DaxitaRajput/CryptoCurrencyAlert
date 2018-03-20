from .views import *
from django.conf.urls import url

urlpatterns = [
	url(r'^$',index,name='index'),
	url(r'^price_alert/$',PriceAlertDetails.as_view(),name='price-alert'),
	url(r'^main_page/$',IndexView.as_view(),name='main-page'),
	url(r'^volume_alert/$',VolumeAlertDetails.as_view(),name='volume-alert'),
	url(r'^marketcap_alert/$',MarketCapAlertDetails.as_view(),name='marketcap-alert'),
	url(r'^pricepercentage_alert/$',PricePercentageAlertDetails.as_view(),name='pricepercentage-alert'),
	url(r'^profitloss_alert/$',ProfitlossAlertDetails.as_view(),name='profitloss-alert'),
]