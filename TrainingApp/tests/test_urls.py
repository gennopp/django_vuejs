from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .. import views


class TestUrls(SimpleTestCase):

    def test_restaurants_url_is_resolved(self):
        url = reverse('restaurants')
        print(resolve(url))
        self.assertEquals(resolve(url).func.__name__, views.RestaurantView.as_view().__name__)

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.__name__, views.HomeView.as_view().__name__)

    def test_order_url_is_resolved(self):
        url = reverse('order', kwargs={'pk': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func.__name__, views.OrderView.as_view().__name__)

    def test_myorder_url_is_resolved(self):
        url = reverse('myorder')
        print(resolve(url))
        self.assertEquals(resolve(url).func.__name__, views.MyOrderView.as_view().__name__)
