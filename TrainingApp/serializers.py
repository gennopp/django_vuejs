from rest_framework import serializers

from .models import Restaurant, Order, Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['name', 'price']
        depth = 2


class RestaurantSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(read_only=True, many=True)

    class Meta:
        fields = '__all__'
        model = Restaurant
        depth = 2


class OrderSerializer(serializers.ModelSerializer):
    dish = DishSerializer(read_only=True, many=True)
    class Meta:
        fields = ['restaurant', 'dish', 'total_price']
        model = Order
        depth = 2
