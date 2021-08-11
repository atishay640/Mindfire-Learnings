from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (ProductViewSet, OrderItemViewSet, OrderViewSet)

router =  SimpleRouter()
router.register('products', ProductViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')
router.register('orderitems', OrderItemViewSet, basename='order-items')

urlpatterns = router.urls