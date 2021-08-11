from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (ProductSerializer, OrderItemSerializer, OrderSerializer)
from .models import (Product, OrderItem, Order)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

