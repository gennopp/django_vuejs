from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework.views import APIView
import json
from rest_framework.decorators import api_view
from .forms import RegisterForm
from .models import Restaurant, Order, Dish
from .serializers import RestaurantSerializer, DishSerializer, OrderSerializer

from django.views.decorators.csrf import csrf_exempt, csrf_protect


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('login'))

    else:
        form = RegisterForm()

    return render(response, "TrainingApp/register.html", {"form": form})


class HomeView(TemplateView):
    template_name = 'TrainingApp/home.html'


class AllRestaurantsView(APIView):
    def get(self, request, format=None):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return JsonResponse(serializer.data, safe=False)


class RestaurantView(APIView):
    def get(self, request, pk):
        restaurant = Restaurant.objects.get(pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return JsonResponse(serializer.data, safe=False)


class AllDishesView(APIView):
    def get(self, request, format=None):
        all_dishes = Dish.objects.all()
        serializer = DishSerializer(all_dishes, many=True)
        return JsonResponse(serializer.data, safe=False)


class DishView(APIView):
    def get(self, request, pk):
        dish = Dish.objects.get(pk=pk)
        serializer = DishSerializer(dish, many=True)
        return JsonResponse(serializer.data, safe=False)

def MyOrderAPIView(request):
	orders = Order.objects.filter(user=request.user)
	serializer = OrderSerializer(orders, many=True)
	return JsonResponse(serializer.data, safe=False)


def MyOrderView(request):
	return render(request, 'TrainingApp/show_order.html')


@csrf_exempt
def PlaceOrdersView(request):

	if request.method == "POST":
		dishes = request.POST
		obj = {}
		for item in dishes.lists():
			obj[item[0]] = item[1]

		rest_id = obj['restaurant'][0]
		restaurant = Restaurant.objects.get(pk=rest_id)
		newOrder = Order.objects.create(user=request.user, restaurant=restaurant)
		price = 0
		for id in obj['dish[]']:
			dish = Dish.objects.get(pk=id)
			price += dish.price
			newOrder.dish.add(dish)

		newOrder.total_price = price
		newOrder.save()

		return redirect('/myorder/')




class OrderView(APIView):
    def get(self, request, pk):
    	restaurant = Restaurant.objects.get(pk=pk)
    	r_dish = restaurant.dishes_served.all()
    	return render(request, 'TrainingApp/order.html', {'r_dish': r_dish})
