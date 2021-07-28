from django.db import models
from django.db.models.deletion import SET_NULL

class Coupon(models.Model):
    fact_order_coupon_order_attribute_key = models.PositiveBigIntegerField(null=True, help_text='Order coupon order attribute key')
    fact_order_coupon_order_date_key = models.PositiveIntegerField(null=True, help_text='Order coupon order date key')
    fact_order_coupon_order_time_key = models.PositiveIntegerField(null=True, help_text='Order coupon order time key')
    fact_order_coupon_coupon_key = models.PositiveIntegerField(null=True, help_text='Order coupon key')
    fact_order_coupon_coupon_quantity = models.PositiveIntegerField(null=True, help_text='Order coupon quantity key')
    fact_order_coupon_coupon_amount = models.PositiveIntegerField(null=True, help_text='Order coupon amount key')
    fact_order_coupon_order_id = models.PositiveIntegerField(null=True, help_text='Order coupon order id')
    fact_order_coupon_date_added = models.DateTimeField(null=True, help_text='Order coupon date added')
    fact_order_coupon_date_modified = models.DateTimeField(null=True, help_text='Order coupon date modified')
    new_coupon_amount = models.PositiveIntegerField(null=True, help_text='Order coupon amount')

class Store(models.Model):
    dim_unit_unit_id= models.PositiveIntegerField(null=True, help_text="Dim Unit unit id")
    dim_coupon_coupon_id = models.PositiveIntegerField(null=True, help_text='Order coupon id')
    dim_coupon_coupon_name = models.CharField(max_length=100, null=True, help_text='Order coupon name')
    coupon = models.ForeignKey(to='Coupon', on_delete=SET_NULL, null=True)

class Order(models.Model):
    uniqueid1= models.CharField(null=True, max_length=150, help_text="Order unique id 1")
    uniqueid2= models.CharField(null=True, max_length=150, help_text="Order unique id 2")
    fact_order_order_key= models.PositiveIntegerField(null=True, help_text="Order key")
    fact_order_Order_Attribute_Key= models.PositiveSmallIntegerField(null=True, help_text="Order attribute key")
    fact_order_Unit_Key= models.PositiveSmallIntegerField(null=True, help_text="Order unit key")
    fact_order_Order_Date_Key= models.PositiveIntegerField(null=True, help_text="Order order date key")
    fact_order_Order_Time_Key= models.PositiveIntegerField(null=True, help_text="Order order time key")
    fact_order_Register_Key= models.PositiveSmallIntegerField(null=True, help_text="Order register key")
    fact_order_Employee_Key= models.IntegerField(null=True, help_text="Order employee key")
    fact_order_Coupon_Amount= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order coupon amount")
    fact_order_Discount_Amount= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order discount amount")
    fact_order_Net_Food_Sales= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order net food sales")
    fact_order_Net_NonFood_Sales= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order unique id 1")
    fact_order_Giftcard_Sales= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order giftcard sales")
    fact_order_Donations= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order donations")
    fact_order_Taxable_Sales= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order taxable sales")
    fact_order_Tax_Collected= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order tax collected")
    fact_order_Total_Order_Amount= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order total order amount")
    fact_order_Item_Count= models.PositiveSmallIntegerField(null=True, help_text="Order item count")
    fact_order_Order_ID= models.PositiveIntegerField(null=True, help_text="Order id")
    fact_order_Date_Added= models.DateTimeField(null=True, help_text="Order date added") 
    fact_order_Date_Modified= models.DateTimeField(null=True, help_text="Order date modified") 
    fact_order_HashValue= models.TextField(null=True, help_text="Order hash value")
    coupon_id_cnt= models.PositiveIntegerField(null=True, help_text="Coupon id cnt")
    fact_order_Net_Food_Sales1= models.DecimalField(max_digits=12,decimal_places=4, null=True, help_text="Order net food sales 1")
    o_startdate= models.PositiveIntegerField(null=True, help_text="Start date")
    o_enddate= models.PositiveIntegerField(null=True, help_text="End date")
    fact_order_DestinationDetail = models.TextField(null=True, help_text='Order Destination detail')




# @shared_task
# def bulk_insert_from_csv():
#     """ The function is used to read csv file in chunks and insert data into database in bulk.
#     """
    
#     print("bulk_insert_from_csv - TRIGGER")
#     # delete existing table records
#     Order.objects.all().delete()

#     start_time = time.time() 
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     filename = f'{dir_path}/../{settings.DPA_RAW_FILE_PATH}'
#     dataframe = pandas.read_csv(filename, chunksize=settings.DPA_CSV_FILE_CHUNK_SIZE, iterator=True, encoding='latin1')
#     dd = defaultdict(list)

#     for chunk in dataframe:
#         sales_data = chunk.to_dict('records', into=dd)
#         print("sales_data size = ", len(sales_data))
#         breakpoint()
#         orders = [Order(
#             uniqueid1 = row.get('uniqueid1'),
#             uniqueid2 = row.get('uniqueid2'),
#             fact_order_order_key = row.get('fact_order_order_key'),
#             fact_order_Order_Attribute_Key = row.get('fact_order_Order_Attribute_Key'),
#             fact_order_Unit_Key = row.get('fact_order_Unit_Key'),
#             dim_unit_unit_id = row.get('dim_unit_unit_id'),
#             fact_order_Order_Date_Key = row.get('fact_order_Order_Date_Key'),
#             fact_order_Order_Time_Key = row.get('fact_order_Order_Time_Key'),
#             fact_order_Register_Key = row.get('fact_order_Register_Key'),
#             fact_order_Employee_Key = row.get('fact_order_Employee_Key'),
#             fact_order_Coupon_Amount = row.get('fact_order_Coupon_Amount'),
#             fact_order_Discount_Amount = row.get('fact_order_Discount_Amount'),
#             fact_order_Net_Food_Sales = row.get('fact_order_Net_Food_Sales'),
#             fact_order_Net_NonFood_Sales = row.get('fact_order_Net_NonFood_Sales'),
#             fact_order_Giftcard_Sales = row.get('fact_order_Giftcard_Sales'),
#             fact_order_Donations = row.get('fact_order_Donations'),
#             fact_order_Taxable_Sales = row.get('fact_order_Taxable_Sales'),
#             fact_order_Tax_Collected = row.get('fact_order_Tax_Collected'),
#             fact_order_Total_Order_Amount = row.get('fact_order_Total_Order_Amount'),
#             fact_order_Item_Count = row.get('fact_order_Item_Count'),
#             fact_order_Order_ID = row.get('fact_order_Order_ID'),
#             fact_order_Date_Added = datetime.strptime(row.get('fact_order_Date_Added'), settings.DPA_DATETIME_INPUT_FORMATS) ,
#             fact_order_Date_Modified = datetime.strptime(row.get('fact_order_Date_Modified'), settings.DPA_DATETIME_INPUT_FORMATS),
#             fact_order_HashValue = row.get('fact_order_HashValue'),
#             coupon_id_cnt = row.get('coupon_id_cnt'),
#             fact_order_Net_Food_Sales1 = row.get('fact_order_Net_Food_Sales1'),
#             o_startdate = row.get('o_startdate'),
#             o_enddate = row.get('o_enddate')) 
#         for row in sales_data]

#         # Adding chunk records in bulk in Database.
#         insert_into_db(orders)
#     print("Time Taken = %s seconds" % (time.time() - start_time))
#     print("bulk_insert_from_csv - FINISHED")