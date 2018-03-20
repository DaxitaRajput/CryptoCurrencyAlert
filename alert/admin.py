from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserTable)
admin.site.register(QueryTable)
admin.site.register(UserPreference)
admin.site.register(CryptoPriceAlert)
admin.site.register(CryptoVolumePrice)
admin.site.register(CryptoMarketCap)