from django.contrib import admin
from . import models as shop


admin.site.register(shop.Order)
admin.site.register(shop.OrderItem)
admin.site.register(shop.Product)
