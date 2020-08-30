from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from TrainingApp.models import Dish, Restaurant, Order
from TrainingApp.views import HomeView, AllRestaurantsView,\
		 OrderView, MyOrderView, AllOrdersView, RestaurantView, AllDishesView
import json
from . import views


class TestUrls(SimpleTestCase):

	def test_restaurants_url_is_resolved(self):
		url = reverse('api-restaurants')
		print(resolve(url))
		self.assertEquals(resolve(url).func.__name__, views.AllRestaurantsView.as_view().__name__)


	def test_home_url_is_resolved(self):
		url = reverse('home')
		print(resolve(url))
		self.assertEquals(resolve(url).func.__name__, views.HomeView.as_view().__name__)


	def test_order_url_is_resolved(self):
		url = reverse('api-orders')
		print(resolve(url))
		self.assertEquals(resolve(url).func, views.AllOrdersView)


	def test_myorder_url_is_resolved(self):
		url = reverse('myorder')
		print(resolve(url))
		self.assertEquals(resolve(url).func, views.MyOrderView)

	def test_api_restaurant_is_resolved(self):
		url = reverse('api-restaurant', kwargs={'pk':1})
		print(resolve(url))
		self.assertEquals(resolve(url).func.__name__, views.RestaurantView.as_view().__name__)

	def test_api_dishes_is_resolved(self):
		url = reverse('api-dishes')
		print(resolve(url))
		self.assertEquals(resolve(url).func.__name__, views.AllDishesView.as_view().__name__)





class TestViews(TestCase):

	def test_home(self):
		client = Client()
		response = client.get(reverse('home'))

		self.assertEquals(response.status_code, 200)

	def test_api_restaurant(self):
		client = Client()
		response = client.get(reverse('api-dishes'))

		self.assertEquals(response.status_code, 200)

	def test_api_restaurants(self):
		client = Client()
		response = client.get(reverse('api-restaurants'))

		self.assertEquals(response.status_code, 200)

