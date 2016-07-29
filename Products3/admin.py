from django.contrib import admin
from django import forms
from Products3.models import *

# Register your models here.

class MetalDetailsInline(admin.TabularInline):
    model = MetalDetails
    min_num = 1
    extra = 0
    fields = ['carats','metal','weight_of_metal','making_charges']


class DiamondDetailsInline(admin.TabularInline):
    model = DiamondDetails
    min_num = 0
    extra = 0
    fields=['diamond_clarity','diamond_color','diamond_shape','number_of_diamonds','weight_of_diamonds','diamond_price']

class GemstoneDetailsInline(admin.TabularInline):
    model = GemstoneDetails
    min_num = 0
    extra = 0
    fields = ['gemstone','gemstone_shape','weight_of_gemstones','gemstone_price']

class ImageDetailsInline(admin.TabularInline):
    model=ImageDetails
    extra=1
    fields=['image']

class ProductAdmin(admin.ModelAdmin):
    fields = (('product_code','product_category','product_type'),'tag')
    inlines = (MetalDetailsInline,DiamondDetailsInline,GemstoneDetailsInline,ImageDetailsInline) 
                

admin.site.register(tags)
admin.site.register(Product,ProductAdmin)
admin.site.register(GoldPrice)
