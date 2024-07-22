from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('craft/', views.craft, name='craft'),
    path('delivery/', views.delivery, name='delivery'),
    path('info/', views.info, name='info'),
    path('cart/', views.cart, name='cart'),
]

