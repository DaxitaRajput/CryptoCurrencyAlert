from django.test import TestCase
from alert.models import *

class CryptoPriceAlertTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# import code; code.interact(local=dict(globals(), **locals()))
		#Set up non-modified objects used by all test methods
		CryptoPriceAlert.objects.create(from_coin_type="BTC",to_coin_type="USD",current_price="123",previous_price="90")

	def test_from_coin_type_label(self):
		c = CryptoPriceAlert.objects.get(id=1)
		field_label = c._meta.get_field('from_coin_type').verbose_name
		self.assertEquals(field_label,'from coin type')

	def test_to_coin_type_label(self):
		c = CryptoPriceAlert.objects.get(id=1)
		field_label = c._meta.get_field('to_coin_type').verbose_name
		self.assertEquals(field_label,'to coin type')

	def test_current_price_label(self):
		c = CryptoPriceAlert.objects.get(id=1)
		field_label = c._meta.get_field('current_price').verbose_name
		self.assertEquals(field_label,'current price')

	def test_previous_price_label(self):
		c = CryptoPriceAlert.objects.get(id=1)
		field_label = c._meta.get_field('previous_price').verbose_name
		self.assertEquals(field_label,'previous price')

	def test_from_coin_type_max_length(self):
		c = CryptoPriceAlert.objects.get(id=1)
		max_length = c._meta.get_field('from_coin_type').max_length
		self.assertEquals(max_length,10)

	def test_to_coin_type_max_length(self):
		c = CryptoPriceAlert.objects.get(id=1)
		max_length = c._meta.get_field('to_coin_type').max_length
		self.assertEquals(max_length,10)

	def test_current_price_max_length(self):
		c = CryptoPriceAlert.objects.get(id=1)
		max_length = c._meta.get_field('current_price').max_length
		self.assertEquals(max_length,20)

	def test_previous_price_max_length(self):
		c = CryptoPriceAlert.objects.get(id=1)
		max_length = c._meta.get_field('previous_price').max_length
		self.assertEquals(max_length,20)

class CryptoVolumePriceTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# import code; code.interact(local=dict(globals(), **locals()))
		#Set up non-modified objects used by all test methods
		CryptoVolumePrice.objects.create(from_coin_type="BTC",to_coin_type="USD",current_volume="123",previous_volume="90")

	def test_from_coin_type_label(self):
		c = CryptoVolumePrice.objects.get(id=1)
		field_label = c._meta.get_field('from_coin_type').verbose_name
		self.assertEquals(field_label,'from coin type')

	def test_to_coin_type_label(self):
		c = CryptoVolumePrice.objects.get(id=1)
		field_label = c._meta.get_field('to_coin_type').verbose_name
		self.assertEquals(field_label,'to coin type')

	def test_current_volume_label(self):
		c = CryptoVolumePrice.objects.get(id=1)
		field_label = c._meta.get_field('current_volume').verbose_name
		self.assertEquals(field_label,'current volume')

	def test_previous_volume_label(self):
		c = CryptoVolumePrice.objects.get(id=1)
		field_label = c._meta.get_field('previous_volume').verbose_name
		self.assertEquals(field_label,'previous volume')

	def test_from_coin_type_max_length(self):
		c = CryptoVolumePrice.objects.get(id=1)
		max_length = c._meta.get_field('from_coin_type').max_length
		self.assertEquals(max_length,10)

	def test_to_coin_type_max_length(self):
		c = CryptoVolumePrice.objects.get(id=1)
		max_length = c._meta.get_field('to_coin_type').max_length
		self.assertEquals(max_length,10)

	def test_current_volume_max_length(self):
		c = CryptoVolumePrice.objects.get(id=1)
		max_length = c._meta.get_field('current_volume').max_length
		self.assertEquals(max_length,20)

	def test_previous_volume_max_length(self):
		c = CryptoVolumePrice.objects.get(id=1)
		max_length = c._meta.get_field('previous_volume').max_length
		self.assertEquals(max_length,20)

class CryptoMarketCapTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# import code; code.interact(local=dict(globals(), **locals()))
		#Set up non-modified objects used by all test methods
		CryptoMarketCap.objects.create(from_coin_type="BTC",to_coin_type="USD",current_marketcap="123",previous_marketcap="90")

	def test_from_coin_type_label(self):
		c = CryptoMarketCap.objects.get(id=1)
		field_label = c._meta.get_field('from_coin_type').verbose_name
		self.assertEquals(field_label,'from coin type')

	def test_to_coin_type_label(self):
		c = CryptoMarketCap.objects.get(id=1)
		field_label = c._meta.get_field('to_coin_type').verbose_name
		self.assertEquals(field_label,'to coin type')

	def test_current_marketcap_label(self):
		c = CryptoMarketCap.objects.get(id=1)
		field_label = c._meta.get_field('current_marketcap').verbose_name
		self.assertEquals(field_label,'current marketcap')

	def test_previous_marketcap_label(self):
		c = CryptoMarketCap.objects.get(id=1)
		field_label = c._meta.get_field('previous_marketcap').verbose_name
		self.assertEquals(field_label,'previous marketcap')

	def test_from_coin_type_max_length(self):
		c = CryptoMarketCap.objects.get(id=1)
		max_length = c._meta.get_field('from_coin_type').max_length
		self.assertEquals(max_length,10)

	def test_to_coin_type_max_length(self):
		c = CryptoMarketCap.objects.get(id=1)
		max_length = c._meta.get_field('to_coin_type').max_length
		self.assertEquals(max_length,10)

	def test_current_marketcap_max_length(self):
		c = CryptoMarketCap.objects.get(id=1)
		max_length = c._meta.get_field('current_marketcap').max_length
		self.assertEquals(max_length,20)

	def test_previous_marketcap_max_length(self):
		c = CryptoMarketCap.objects.get(id=1)
		max_length = c._meta.get_field('previous_marketcap').max_length
		self.assertEquals(max_length,20)

class UserTableTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# import code; code.interact(local=dict(globals(), **locals()))
		#Set up non-modified objects used by all test methods
		UserTable.objects.create(email_id="big@gmail.com")

	def test_email_id_label(self):
		user = UserTable.objects.get(email_id="big@gmail.com")
		field_label = user._meta.get_field('email_id').verbose_name
		self.assertEquals(field_label,'email id')

	def test_email_id_max_length(self):
		user = UserTable.objects.get(email_id="big@gmail.com")
		max_length = user._meta.get_field('email_id').max_length
		self.assertEquals(max_length,50)

class QueryTableTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# import code; code.interact(local=dict(globals(), **locals()))
		#Set up non-modified objects used by all test methods
		user = UserTable.objects.create(email_id="big@gmail.com")
		QueryTable.objects.create(userid=user,dynamic_query="select * from alert_cryptopricealert;")

	def test_dynamic_query_label(self):
		q = QueryTable.objects.get(id=1)
		field_label = q._meta.get_field('dynamic_query').verbose_name
		self.assertEquals(field_label,'dynamic query')

class UserPreferenceTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# import code; code.interact(local=dict(globals(), **locals()))
		#Set up non-modified objects used by all test methods
		user = UserTable.objects.create(email_id="big@gmail.com")
		UserPreference.objects.create(userid=user,json_data='{"previous_price":"2131","from_coin_type":"BTC","to_coin_type":"USD","current_price":"4589"}')

	def test_json_data_label(self):
		q = UserPreference.objects.get(id=1)
		field_label = q._meta.get_field('json_data').verbose_name
		self.assertEquals(field_label,'json data')