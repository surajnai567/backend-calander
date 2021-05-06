from django.contrib import admin
from .models import Order, OrderDetail

# Register your models here.


@admin.register(Order)
class Order(admin.ModelAdmin):
	list_display = ['date', 'mobile', 'area', 'address', 'status', 'item_list']
	list_editable = ['status']

@admin.register(OrderDetail)
class OrderDetail(admin.ModelAdmin):
	list_display = ['order_id', 'itemname', 'itemquantity', 'itemprice', 'itemtotal']



