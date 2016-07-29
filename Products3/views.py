from django.shortcuts import render

# Create your views here.            	     
# def product_detail_page(request,code):
# 	current_product_code=Product.objects.get(product_code=code)
# 	product_id=current_product_code.id
# 	metal_data=MetalDetails.objects.filter(product=product_id)
#     diamond_data=MetalDetails.objects.filter(product=product_id)
#     gemstone_data=GemstoneDetails.objects.filter(product=product_id)
#     metal_cost=0
#     making_charges=0
#     diamond_charges=0
#     gemstone_charges=0
#     total_charges=0
#     if metal_data:
#     	for i in metal_data:
#     		gold_price=GoldPrice.objects.get(id=1).price_per_gm_24_kt
#     		making_charges=making_charges+i.weight_of_metal*gold_price*i.making_percentage
#     		if i.carats=='22':
#     			gold_price=GoldPrice.objects.get(id=1).price_per_gm_22_kt
#     		elif i.carats=='18':
#     		    gold_price=GoldPrice.objects.get(id=1).price_per_gm_18_kt
#     		elif i.carats=='14':
#     		    gold_price=GoldPrice.objects.get(id=1).price_per_gm_14_kt    	
#     		metal_cost=i.weight_of_metal*gold_price
#     if diamond_data:
#     	for i in diamond_data:
#     		diamond_charges=diamond_charges+i.diamond_price
#     if gemstone_data:
#     	for i in gemstone_data:
#     		gemstone_charges=gemstone_charges+i.gemstone_price
    
#     total_charges=metal_cost+making_charges+diamond_charges+gemstone_charges
#     data={'total_charges':total_charges}
#     return render(request,'',data)     



    		    
 