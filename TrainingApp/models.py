from django.contrib.auth.models import User
from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(default=0)

    # def __iter__(self):
    #     return [self.name, self.price] 

    def __str__(self):
        return str(self.name)

class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    dishes_served = models.ManyToManyField(Dish)

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish = models.ManyToManyField(Dish)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
