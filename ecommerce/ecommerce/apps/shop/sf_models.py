from salesforce import models
from django.contrib.auth.models import User

class ProductSF(models.Model):

    id = models.CharField(primary_key=True, max_length=20, editable=True)
    is_active = models.BooleanField(db_column='IsActive', verbose_name='Active', default=True)
    created_by = models.CharField( max_length=20, db_column='CreatedById')
    sku = models.CharField(db_column='StockKeepingUnit', max_length=180, sf_read_only=models.READ_ONLY)
    name = models.CharField(db_column='Name', max_length=255)
    description = models.TextField(db_column='Description', max_length=4000)
    created_date = models.DateTimeField(db_column='CreatedDate', sf_read_only=models.READ_ONLY)
    last_modified_date = models.DateTimeField(db_column='LastModifiedDate', sf_read_only=models.READ_ONLY)

    class Meta(models.Model.Meta):
        db_table = 'Product2'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class AccountSF(models.Model):
    is_deleted = models.BooleanField(db_column='IsDeleted', verbose_name='Deleted', sf_read_only=models.READ_ONLY, default=False)
    name = models.CharField(db_column='Name', max_length=255, verbose_name='Account Name')
    type = models.CharField(db_column='Type', max_length=255, verbose_name='Account Type', choices=[('Prospect', 'Prospect'), ('Customer - Direct', 'Customer - Direct'), ('Customer - Channel', 'Customer - Channel'), ('Channel Partner / Reseller', 'Channel Partner / Reseller'), ('Installation Partner', 'Installation Partner'), ('Technology Partner', 'Technology Partner'), ('Other', 'Other')], blank=True, null=True)

    class Meta(models.Model.Meta):
        db_table = 'Account'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'


class OrderSF(models.Model):

    account = models.ForeignKey(AccountSF, models.DO_NOTHING, db_column='AccountId', verbose_name='Account ID', blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=100, choices=[('Draft', 'Draft'), ('Activated', 'Activated')])
    name = models.CharField(db_column='Name', max_length=80, verbose_name='Order Name', blank=True, null=True)
    order_number = models.CharField(db_column='OrderNumber', max_length=30, sf_read_only=models.READ_ONLY)
    total_amount = models.DecimalField(db_column='TotalAmount', max_digits=18, decimal_places=2, verbose_name='Order Amount', sf_read_only=models.READ_ONLY)
    created_date = models.DateTimeField(db_column='CreatedDate', sf_read_only=models.READ_ONLY)
    created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='CreatedById', related_name='order_createdby_set', verbose_name='Created By ID', sf_read_only=models.READ_ONLY, null=True)
    is_deleted = models.BooleanField(db_column='IsDeleted', verbose_name='Deleted', sf_read_only=models.READ_ONLY, default=False)
    shipping_street = models.TextField(db_column='ShippingStreet', blank=True, null=True)
    shipping_city = models.CharField(db_column='ShippingCity', max_length=40, blank=True, null=True)
    shipping_state = models.CharField(db_column='ShippingState', max_length=80, verbose_name='Shipping State/Province', blank=True, null=True)
    shipping_postal_code = models.CharField(db_column='ShippingPostalCode', max_length=20, verbose_name='Shipping Zip/Postal Code', blank=True, null=True)
    shipping_country = models.CharField(db_column='ShippingCountry', max_length=80, blank=True, null=True)
    shipping_latitude = models.DecimalField(db_column='ShippingLatitude', max_digits=18, decimal_places=15, blank=True, null=True)
    shipping_longitude = models.DecimalField(db_column='ShippingLongitude', max_digits=18, decimal_places=15, blank=True, null=True)
    shipping_geocode_accuracy = models.CharField(db_column='ShippingGeocodeAccuracy', max_length=40, choices=[('Address', 'Address'), ('NearAddress', 'NearAddress'), ('Block', 'Block'), ('Street', 'Street'), ('ExtendedZip', 'ExtendedZip'), ('Zip', 'Zip'), ('Neighborhood', 'Neighborhood'), ('City', 'City'), ('County', 'County'), ('State', 'State'), ('Unknown', 'Unknown')], blank=True, null=True)
    shipping_address = models.TextField(db_column='ShippingAddress', sf_read_only=models.READ_ONLY, blank=True, null=True)  # This field type is a guess.
    effective_date = models.DateField(db_column='EffectiveDate', verbose_name='Order Start Date')

    class Meta(models.Model.Meta):
        db_table = 'Order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItemSF(models.Model):

    id = models.CharField(primary_key=True, max_length=20, editable=True)
    product = models.ForeignKey(ProductSF, models.DO_NOTHING, db_column='Product2Id', verbose_name='Product ID', sf_read_only=models.NOT_UPDATEABLE, blank=True, null=True)
    order = models.ForeignKey(OrderSF, models.DO_NOTHING, db_column='OrderId', verbose_name='Order ID', sf_read_only=models.NOT_UPDATEABLE)  # Master Detail Relationship *
    quantity = models.DecimalField(db_column='Quantity', max_digits=18, decimal_places=2)
    total_price = models.DecimalField(db_column='TotalPrice', max_digits=18, decimal_places=2, sf_read_only=models.READ_ONLY, blank=True, null=True)
    created_date = models.DateTimeField(db_column='CreatedDate', sf_read_only=models.READ_ONLY)
    created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='CreatedById', related_name='orderitem_createdby_set', verbose_name='Created By ID', sf_read_only=models.READ_ONLY)
    
    class Meta(models.Model.Meta):
        db_table = 'OrderItem'
        verbose_name = 'Order Product'
        verbose_name_plural = 'Order Products'