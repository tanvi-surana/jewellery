from django.shortcuts import render,redirect
from Products.models import *
from roughViews.forms import filterForm
from django.http import HttpResponse
from django.core import serializers
from django.apps import apps
from Products3.models import *


# Create your views here.
def initialPage(request):
	return render(request,'initialPage/initialPageAccordian.html',{})

def jwelleryPage(request):
	return render(request,'jwelleryPage/jwelleryPage.html',{"page":"jwellery"})

def solitaresPage(request):
	return render(request,'jwelleryPage/jwelleryPage.html',{"page":"solitares"})

def goldCoinsPage(request):
	return render(request,'jwelleryPage/jwelleryPage.html',{"page":"goldCoins"})

def collectionsPage(request):
	return render(request,'jwelleryPage/jwelleryPage.html',{"page":"collections"})

def giftsPage(request):
	return render(request,'jwelleryPage/jwelleryPage.html',{"page":"gifts"})

def productPage(request):
	identifier=request.GET.get('identifier').title()
	products=Product.objects.filter(product_category=identifier)
	print(products)
	return render(request,'jwelleryProductPage/jewlleryProductPage.html',{"page":"jwellery","products":products})

def footer(request):
	return render(request,'footer/footer.html')


#def product_detail_page(request):
#	return render(request,'product_detail/product_detail.html',{})

def product_detail_page(request,code):
	current_product_code=Product.objects.get(product_code=code)
	product_id=current_product_code.id
	metal_data=MetalDetails.objects.filter(product=product_id)
	diamond_data=DiamondDetails.objects.filter(product=product_id)
	gemstone_data=GemstoneDetails.objects.filter(product=product_id)
	image_data=ImageDetails.objects.filter(product=product_id)
	metal_cost=0
	making_charges=0
	diamond_charges=0
	gemstone_charges=0
	total_charges=0
	total_diamond_weight=0
	metal_weight=0
	metal_type=''
	metal_kt=''
	diamond_color=''
	diamond_clarity=''
	if metal_data:
		for i in metal_data:
			gold_price=GoldPrice.objects.get(id=1).price_per_gm_24_kt
			metal_weight=metal_weight+i.weight_of_metal
			metal_type=i.metal
			making_charges=making_charges+i.weight_of_metal*gold_price*i.making_charges/100
			if i.carats=='22':
				gold_price=GoldPrice.objects.get(id=1).price_per_gm_22_kt
				metal_kt=i.carats
			elif i.carats=='18':
				gold_price=GoldPrice.objects.get(id=1).price_per_gm_18_kt
				metal_kt=i.carats
			elif i.carats=='14':
				gold_price=GoldPrice.objects.get(id=1).price_per_gm_14_kt
				metal_kt=i.carats
			metal_cost=i.weight_of_metal*gold_price 

	if diamond_data:
		for i in diamond_data:
			diamond_charges=diamond_charges+i.diamond_price*i.weight_of_diamonds     #price is per carat
			total_diamond_weight=total_diamond_weight+i.weight_of_diamonds

	if gemstone_data:
		for i in gemstone_data:
			gemstone_charges=gemstone_charges+i.gemstone_price*i.weight_of_gemstones #price is per carat


	total_charges=metal_cost+making_charges+diamond_charges+gemstone_charges
	product_category=current_product_code.product_category
	data={'total_charges':total_charges,'metal_type':metal_type,'product_code':current_product_code,
	'product_category':product_category,'metal_karat':metal_kt,'metal_weight':metal_weight,
	'diamond_weight':total_diamond_weight,'diamond_color':diamond_color,
	'diamond_clarity':diamond_clarity,'diamond_data':diamond_data,
	'gemstone_data':gemstone_data,'image_data':image_data}
	return render(request,'product_detail/product_detail.html',data)


def account_create(request):
	return render(request,'account-create/account-create.html',{})

def order_payment(request):
	return render(request,'order-payment/order-payment.html',{})
 