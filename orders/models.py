from django.db import models
from django.contrib.auth.models import User
from Products3.models import *
# Create your models here.

class orderDeliveryDetails(models.Model):
	phone = models.CharField(max_length=12,default='')
	street_address = models.CharField(max_length = 100, null=True, blank=True)
	city = models.CharField(max_length=20,blank=True, null=True)
	pincode = models.CharField(max_length=8, default="0000000")

class order(models.Model):
	user=models.OneToOneField(User)
	orderId=models.CharField(max_length=15)  # create at run time
	productCode=models.ForeignKey(Product)
	orderPlacedDate=models.DateTimeField(auto_now=True)
	deliveryDate=models.DateField(null=True)
	orderDelivered=models.BooleanField(default=False)
	orderCancelled=models.BooleanField(default=False)
	isBasicAddress=models.BooleanField(default=True)
	isNotBasicAddress=models.ForeignKey(orderDeliveryDetails,blank=True,null=True)
	orderAmount=models.IntegerField()
	def __str__(self):
		return self.orderId