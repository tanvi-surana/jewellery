from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django import forms
from django.db import models
from Products2.models import *
from django.forms import CheckboxSelectMultiple
from django.apps import apps

# Register your models here.
#------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Form For Admin Site------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

class ProductForm(forms.ModelForm):
	def clean_product_code(self):#------------------------------------------Cleaning Product code for uniqueness of object#
		productCodeChanged=False
		changedData=self.changed_data
		for d in changedData:
			if d=='product_code':
				productCodeChanged=True
		if productCodeChanged:
			productCode=self.cleaned_data['product_code']
			products=[]
			app=apps.get_app_config('Products2')
			models=app.models.values()
			for model in models:
				flag=True
				fields=model._meta.get_all_field_names()
				for field in fields:
					if field=='product_code':
						products+=model.objects.filter(product_code=product_code)
						if model.objects.filter(product_code=product_code):
							flag=False
							break
				if not flag:
					break
			if(len(products) is not 0):
				self._errors['product_code']=self.error_class(["Product with this Product Code already exists"])
				raise forms.ValidationError("")
			else:
				return self.cleaned_data['product_code']
		else:
			return self.cleaned_data['product_code']


#-------------------------------------------------------X-X-X------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------Inline Models----------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

class metalDetailsInline(admin.TabularInline):
	model=metalDetails
	min_num=1
	extra = 0
	fields=['carats','metal','weight_of_metal','price_for_metal']
	filter_horizontal_checkbox = ('carats',)
	formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple}}

class diamondDetailsInline(admin.TabularInline):
    model = diamondDetails
    extra = 1
    fields=['diamond_clarity','diamond_color','diamond_shape','number_of_diamonds','weight_of_diamonds','diamond_price']


class gemstoneDetailInline(admin.TabularInline):
    model = gemstoneDetails
    extra = 1
    fields=['gemstone','gemstone_shape','number_of_gemstones','gemstone_price']

class photosInline(admin.TabularInline):
	model=PHOTOS
	extra=0
	min_num=1
	fields=['photo']

#-------------------------------------------------------X-X-X------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------Admin Product View------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

class EarringProductAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'jQuery/jquery-1.11.2.min.js',
            'jquery-tokeninput/src/jquery.tokeninput.js',
            'adminSite/js/adminSiteTokenizing.js',
        )

    form = ProductForm
    fields = (('product_code','product_type'),'making_charges','tag')
    inlines = (metalDetailsInline,diamondDetailsInline,gemstoneDetailInline,photosInline)

class BangleProductAdmin(admin.ModelAdmin):
	form = ProductForm
	fields = (('product_code','product_type'),'making_charges','tag')
	inlines = (metalDetailsInline,diamondDetailsInline,gemstoneDetailInline,photosInline)

class RingProductAdmin(admin.ModelAdmin):
	form = ProductForm
	fields = (('product_code','product_type'),'making_charges','tag')
	inlines = (metalDetailsInline,diamondDetailsInline,gemstoneDetailInline,photosInline)

class BraceletProductAdmin(admin.ModelAdmin):
	form = ProductForm
	fields = (('product_code','product_type'),'making_charges','tag')
	inlines = (metalDetailsInline,diamondDetailsInline,gemstoneDetailInline,photosInline)

class NosepinProductAdmin(admin.ModelAdmin):
	form = ProductForm
	fields = (('product_code','product_type'),'making_charges','tag')
	inlines = (metalDetailsInline,diamondDetailsInline,gemstoneDetailInline,photosInline)

class NecklaceProductAdmin(admin.ModelAdmin):
	form = ProductForm
	fields = (('product_code','product_type'),'making_charges','tag')
	inlines = (metalDetailsInline,diamondDetailsInline,gemstoneDetailInline,photosInline)

class MangalsutraProductAdmin(admin.ModelAdmin):
	form = ProductForm
	fields = (('product_code','product_type'),'making_charges','tag')
	inlines = (metalDetailsInline,diamondDetailsInline,gemstoneDetailInline,photosInline)


#-------------------------------------------------------X-X-X------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------Registering-------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

#admin.site.register(DIAMOND)
admin.site.register(GEMSTONES)
admin.site.register(METAL)
admin.site.register(METALCARAT)
admin.site.register(tags)
admin.site.register(earringProduct,EarringProductAdmin)
admin.site.register(bangleProduct,BangleProductAdmin)
admin.site.register(ringProduct,RingProductAdmin)
admin.site.register(braceletProduct,BraceletProductAdmin)
admin.site.register(nosepinProduct,NosepinProductAdmin)
admin.site.register(necklaceProduct,NecklaceProductAdmin)
admin.site.register(mangalsutraProduct,MangalsutraProductAdmin)

#-------------------------------------------------------X-X-X------------------------------------------------------------#
