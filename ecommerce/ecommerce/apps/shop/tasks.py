from celery import shared_task
from apps.shop import sf_models
from django.conf import settings
from apps.shop import models


@shared_task
def sync_products_from_salesforce():
    DB_PRODUCT_QUERYSET = models.Product.objects.using(
        settings.DJANGO_DB_ROUTE)
    SF_PRODUCT_QUERYSET = sf_models.ProductSF.objects.using(
        settings.SALSEFORCE_DB_ROUTE)

    is_products = DB_PRODUCT_QUERYSET.exists()
    if is_products:
        last_product = DB_PRODUCT_QUERYSET.order_by('created_date').last()
        print(
            f"Collecting products created after : {last_product.created_date} from SF DB")
        sf_products = SF_PRODUCT_QUERYSET.filter(created_date__gt=last_product.created_date).values('sku', 'name', 'description', 'is_active',
                                                                                                    'created_date', 'last_modified_date')
    else:
        print("Collecting products all from SF DB")
        sf_products = SF_PRODUCT_QUERYSET.values('sku', 'name', 'description', 'is_active',
                                                 'created_date', 'last_modified_date')

    if sf_products:
        new_products = [models.Product(**product) for product in sf_products]
        DB_PRODUCT_QUERYSET.bulk_create(new_products)
        print(f"Created {len(sf_products)} products in Django DB.")
    else:
        print("No new product found.")
        return


@shared_task
def sync_orders_to_saleforce():
    DB_ORDER_QUERYSET = models.Order.objects.using(settings.DJANGO_DB_ROUTE)
    SF_ORDER_QUERYSET = sf_models.OrderSF.objects.using(
        settings.SALSEFORCE_DB_ROUTE)
    SF_ACCOUNT_QUERYSET = sf_models.AccountSF.objects.using(
        settings.SALSEFORCE_DB_ROUTE)

    is_orders = SF_ORDER_QUERYSET.exists()
    if is_orders:
        last_order = SF_ORDER_QUERYSET.order_by('created_date').last()
        print(last_order.name)
        print(
            f"Collecting orders created after : {last_order.created_date} from SF DB")
        db_orders = DB_ORDER_QUERYSET.filter(created_date__gt=last_order.created_date).values('status', 'effective_date', 'name', 'total_amount', 'shipping_street', 'shipping_city',
                                                                                                                   'shipping_state', 'shipping_postal_code', 'shipping_country', 'shipping_latitude',
                                                                                                                   'shipping_longitude', 'shipping_geocode_accuracy', 'shipping_address', 'effective_date')
    else:
        print("Collecting orders all from Django DB")
        db_orders = DB_ORDER_QUERYSET.values('status', 'effective_date', 'name', 'total_amount', 'shipping_street', 'shipping_city', 'shipping_state',
                                             'shipping_postal_code', 'shipping_country', 'shipping_latitude', 'shipping_longitude', 'shipping_geocode_accuracy', 'shipping_address', 'effective_date')

    if db_orders:
        new_orders = [sf_models.OrderSF(
            **order, account=SF_ACCOUNT_QUERYSET.first()) for order in db_orders]
        SF_ORDER_QUERYSET.bulk_create(new_orders)
        print(f"Created {len(db_orders)} orders in SF DB.")
    else:
        print("No new order found.")
        return
