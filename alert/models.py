""" This file describes the tables or models used for entire application. """
from django.db import models


"""This is for crypto price alert"""
class CryptoPriceAlert(models.Model):
    from_coin_type = models.CharField(max_length=10)
    to_coin_type = models.CharField(max_length=10)
    current_price = models.CharField(max_length=20)
    previous_price = models.CharField(max_length=20)

    def __str__(self):
        return self.from_coin_type

"""
This is for crypto volume alert
"""
class CryptoVolumePrice(models.Model):
    from_coin_type = models.CharField(max_length=10)
    to_coin_type = models.CharField(max_length=10)
    current_volume = models.CharField(max_length=20)
    previous_volume = models.CharField(max_length=20)

    def __str__(self):
        return self.from_coin_type

"""
This is for crypto marketcap alert
"""
class CryptoMarketCap(models.Model):
    from_coin_type = models.CharField(max_length=10)
    to_coin_type = models.CharField(max_length=10)
    current_marketcap = models.CharField(max_length=20)
    previous_marketcap = models.CharField(max_length=20)

    def __str__(self):
        return self.from_coin_type

"""
This is for user data
"""

class UserTable(models.Model):
    email_id = models.EmailField(max_length=50)


"""
This is for dynamic query data
"""

class QueryTable(models.Model):
    userid = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    dynamic_query = models.TextField()

"""
This is for user preferences
"""

class UserPreference(models.Model):
    userid = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    json_data = models.TextField()
