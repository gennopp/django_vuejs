from django.urls import path

from . import views

urlpatterns = [
    path('api/restaurants/', views.AllRestaurantsView.as_view(), name='api-restaurants'),
    path('api/restaurant/<int:pk>/', views.RestaurantView.as_view(), name='api-restaurant'),
    path('api/dishes/', views.AllDishesView.as_view(), name='api-dishes'),
    path('api/dish/<int:pk>/', views.DishView.as_view(), name='api-dish'),
    path('api/orders/', views.PlaceOrdersView, name='orders'),
    path('api/order/<int:pk>/', views.OrderView.as_view(), name='api-order'),


    path('', views.HomeView.as_view(), name='home'),
    path('api/myorder/', views.MyOrderAPIView, name='api-myorder'),
    path('myorder/', views.MyOrderView, name='myorder'),
    path('register/', views.register, name='register'),
]
