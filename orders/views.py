from django.shortcuts import render
from rest_framework import generics
from .serializers import OrderSerializer
from .models import Order

class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

