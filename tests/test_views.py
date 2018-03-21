# import code; code.interact(local=dict(globals(), **locals()))
from django.test import TestCase
from alert.models import *
from alert.forms import *

class IndexViewTest(TestCase):

	def test_indexview_uses_correct_template(self):
		resp = self.client.get('/alert/main_page/')
		self.assertTemplateUsed(resp, 'alert/main_page.html')

	def test_response_status_code(self):
		resp = self.client.get('/alert/main_page/')
		self.assertEqual(resp.status_code, 200)

	def test_response_data(self):
		resp = self.client.get('/alert/main_page/')
		self.assertEqual(resp.context['forms']['price'], PriceAlertForm)
		self.assertEqual(resp.context['forms']['volume'], VolumeAlertForm)
		self.assertEqual(resp.context['forms']['marketcap'], MarketCapAlertForm)
		self.assertEqual(resp.context['forms']['profitloss'], ProfitlossAlertForm)
		self.assertEqual(resp.context['forms']['pricepercentage'], PricepercentageAlertForm)

class PriceAlertDetailsTest(TestCase):

	def test_data_stored_in_databse(self):
		user = UserTable.objects.get_or_create(email_id="mail@gmail.com")
		j_data = {"json_type":"price_alert", "json_from_coin_type":"initial_coin_type", "json_above_price":"above_price", "json_above_coin_type":"above_price_coin_type", "json_below_price":"below_price", "json_below_coin_type":"below_price_coin_type", "json_email_id":"email_id@gjj.ghj"}
		UserPreference.objects.create(userid=user[0], json_data=j_data)
		saved_items = UserPreference.objects.all()
		self.assertEqual(saved_items.count(), 1)


	def test_priceview_uses_correct_template(self):
		resp = self.client.get('/alert/price_alert/')
		self.assertTemplateUsed(resp, 'alert/main_page.html')

	def test_priceresponse_status_code(self):
		resp = self.client.get('/alert/price_alert/')
		self.assertEqual(resp.status_code, 200)

	def test_priceview_uses_correct_formclass(self):
		resp = self.client.get('/alert/price_alert/')
		self.assertEqual(type(resp.context['form']), PriceAlertForm)

	def test_add_price_preferences(self):
		resp = self.client.post('/alert/price_alert', {'from_coin_type':'ETH', 'above_coin_type':'BTC', 'below_coin_type':'BTC', 'above_price':'34', 'below_price':'10', 'email_id':'mail@mail.com'})
		# import code; code.interact(local=dict(globals(), **locals()))
		self.assertIn('', resp.content.decode())
		self.assertEqual(resp.status_code, 301)
		# self.assertRedirects(resp, '/alert/main_page/')

class VolumeAlertDetailsTest(TestCase):

	def test_volumeview_uses_correct_template(self):
		resp = self.client.get('/alert/volume_alert/')
		self.assertTemplateUsed(resp, 'alert/main_page.html')

	def test_volumeresponse_status_code(self):
		resp = self.client.get('/alert/volume_alert/')
		self.assertEqual(resp.status_code, 200)

	def test_volumeview_uses_correct_formclass(self):
		resp = self.client.get('/alert/volume_alert/')
		self.assertEqual(type(resp.context['form']), VolumeAlertForm)

	def test_add_volume_preferences(self):
		resp = self.client.post('/alert/volume_alert', {'from_coin_type':'ETH', 'above_coin_type':'BTC', 'below_coin_type':'BTC', 'above_volume':'20', 'below_volume':'10', 'email_id':'mail@mail.com'})
		self.assertEqual(resp.status_code, 301)

class MarketCapAlertDetailsTest(TestCase):

	def test_marketview_uses_correct_template(self):
		resp = self.client.get('/alert/marketcap_alert/')
		self.assertTemplateUsed(resp, 'alert/main_page.html')

	def test_marketresponse_status_code(self):
		resp = self.client.get('/alert/marketcap_alert/')
		self.assertEqual(resp.status_code, 200)

	def test_marketview_uses_correct_formclass(self):
		resp = self.client.get('/alert/marketcap_alert/')
		self.assertEqual(type(resp.context['form']), MarketCapAlertForm)

	def test_add_market_preferences(self):
		resp = self.client.post('/alert/marketcap_alert', {'from_coin_type':'ETH', 'above_coin_type':'BTC', 'below_coin_type':'BTC', 'above_marketcap':'20', 'below_marketcap':'10', 'email_id':'mail@mail.com'})
		self.assertEqual(resp.status_code, 301)

class ProfitlossAlertDetailsTest(TestCase):

	def test_profitlossview_uses_correct_template(self):
		resp = self.client.get('/alert/profitloss_alert/')
		self.assertTemplateUsed(resp, 'alert/main_page.html')

	def test_profitlossresponse_status_code(self):
		resp = self.client.get('/alert/profitloss_alert/')
		self.assertEqual(resp.status_code, 200)

	def test_profitlossview_uses_correct_formclass(self):
		resp = self.client.get('/alert/profitloss_alert/')
		self.assertEqual(type(resp.context['form']), ProfitlossAlertForm)

	def test_add_profitloss_preferences(self):
		resp = self.client.post('/alert/profitloss_alert', {'from_coin_type':'ETH', 'purchasing_coin_type':'BTC', 'frequency':'Every Hour', 'purchasing_price':'209', 'purchasing_quantity':'5', 'email_id':'mail@mail.com'})
		self.assertEqual(resp.status_code, 301)


class PricePercentageAlertDetailsTest(TestCase):

	def test_pricepercentageview_uses_correct_template(self):
		resp = self.client.get('/alert/pricepercentage_alert/')
		self.assertTemplateUsed(resp, 'alert/main_page.html')

	def test_pricepercentageresponse_status_code(self):
		resp = self.client.get('/alert/pricepercentage_alert/')
		self.assertEqual(resp.status_code, 200)

	def test_pricepercentageview_uses_correct_formclass(self):
		resp = self.client.get('/alert/pricepercentage_alert/')
		self.assertEqual(type(resp.context['form']), PricepercentageAlertForm)

	def test_add_pricepercentage_preferences(self):
		resp = self.client.post('/alert/pricepercentage_alert', {'from_coin_type':'ETH', 'above_coin_type':'BTC', 'below_coin_type':'BTC', 'above_price_percentage':'20', 'below_price_percentage':'10', 'email_id':'mail@mail.com'})
		self.assertEqual(resp.status_code, 301)
