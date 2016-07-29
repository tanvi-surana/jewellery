from django.contrib import admin
from orders.models import *
# Register your models here.
admin.site.register(order)
admin.site.register(orderDeliveryDetails)