from .views import *
from django.conf.urls import url

urlpatterns = [
	url(r'^$',index,name='index')
]