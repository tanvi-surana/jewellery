from django.db import models

# Create your models here.

#----------------------------------------------------------------------------------------------------------------#
#--------------------------------------------Metal,Diamond,Gemstones---------------------------------------------#
#----------------------------------------------------------------------------------------------------------------#

#-------------------------------------Information About models which are linked as ManyToManyField to products using through through fields of through fields of their details
class METAL(models.Model):
    metal_choices=(('Yellow Gold','Yellow Gold'),('White Gold','White Gold'))
    metal=models.CharField(max_length=15,choices=metal_choices,null=True,blank=False,unique=True)

    def __str__(self):
        return self.metal

    class Meta:
        verbose_name = 'METAL'
        verbose_name_plural='METALS'
        ordering = ['-metal']

class METALCARAT(models.Model):
    carat_choices=(('14','14'),('16','16'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'))
    carats=models.CharField(max_length=2,choices=carat_choices,null=True,blank=False,unique=True)
    def __str__(self):
        return self.carats

    class Meta:
        verbose_name = 'CARAT'
        verbose_name_plural='CARTATS'
        ordering=['carats']


class DIAMOND(models.Model):
    clarity_choices=(('FL','FL'),('IF','IF'),('VVS1','VVS1'),('VVS2','VVS2'),('SI1','SI1'),('SI2','SI2'),('I1','I1'),('I2','I2'),('I3','I3'))
    diamond_clarity=models.CharField(max_length=4,choices=clarity_choices,blank=True,null=True,unique=True)
    def __str__(self):
        if self is None:
            return 'None'
        else:
            return self.diamondClarity

    class Meta:
        verbose_name = 'Earing Product'
        verbose_name_plural='DIAMONDS'
        ordering=['pk']


class GEMSTONES(models.Model):
    stone_choices=(('Emerald','Emerald'),('Ruby','Ruby'),('Amethyst','Amethyst'),('Pink Tourmaline','Pink Tourmaline'),('Garnet','Garnet'),('Citrine','Citrine'),('Pearls','Pearls'),('Blue Topaz','Blue Topaz'),('Saphire','Saphire'),('Iolite','Iolite'))
    gemstone=models.CharField(max_length=20,choices=stone_choices,null=True,blank=False,unique=True)
    def __str__(self):
        return self.gemstone

    class Meta:
        verbose_name = 'GEMSTONE'
        verbose_name_plural='GEMSTONES'
        ordering=['pk']



#--------------------------------------------------X-X-X---------------------------------------------------------#



#----------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Products-----------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------#

class tags(models.Model):
    tagName=models.CharField(max_length=20,null=True,blank=False,default='')
    def __str__(self):
        return self.tagName

    class Meta:
        verbose_name_plural='Tags'


class earringProduct(models.Model):#---------------------------------------------------Earing
    product_code = models.CharField(max_length=10,null=True,blank=False,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    product_type_choice = (('Other','Other'),('Studs','Studs'),('Polki','Polki'),('Drops','Drops'),('Hoops','Hoops'),('Jhumki','Jhumki'),('Sui-Dhaga','Sui-Dhaga'),('Cluster','Cluster'),('Chand Bali','Chand Bali'))
    product_type = models.CharField(max_length=20,choices=product_type_choice,null=True,blank=False,default='')
    tag = models.ManyToManyField(tags,related_name='earringTAGS',blank=True)
    metal = models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('earring','carats'),related_name='earingMetal',blank=False)
    making_charges = models.IntegerField(blank=False,null=True)
    #diamond = models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('earring','diamond'),related_name='earingDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    #gemstones = models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('earring','gemstone'),related_name='earingGemstone')
    def __str__(self):
        return self.productType+" / "+self.productCode

    class Meta:
        verbose_name = "Earring Product"
        verbose_name_plural = "Earring Products"
        ordering=['product_code']

class bangleProduct(models.Model):#--------------------------------------------------Bangle
    product_code = models.CharField(max_length=10,null=True,blank=False,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    product_type_choice = (('Other','Other'),('Round','Round'),('Oval','Oval'),('Gold','Gold'),('Bridal','Bridal'))
    product_type = models.CharField(max_length=20,choices=product_type_choice,null=True,blank=False,default='')
    tag = models.ManyToManyField(tags,related_name='bangleTAGS',blank=True)
    metal = models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('bangle','carats'),related_name='bangleMetal')
    making_charges = models.IntegerField(blank=False,null=True)
    #diamond=models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('bangle','diamond'),related_name='bangleDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    #gemstones = models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('bangle','gemstone'),related_name='bangleGemstone')
    def __str__(self):
        return self.product_type+" / "+self.product_code

    class Meta:
        verbose_name = "Bangle Product"
        verbose_name_plural = "Bangle Products"
        ordering=['product_code']

class ringProduct(models.Model):#-------------------------------------------------------Ring
    product_code = models.CharField(max_length=10,null=True,blank=False,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    product_type_choice = (('Other','Other'),('Engagement','Engagement'),('Couple Bands','Couple Bands'),('Navratna','Navratna'),('Cocktail','Cocktail'),('Platinum','Platinum'))
    product_type = models.CharField(max_length=20,choices=product_type_choice,null=True,blank=False,default='')
    tag = models.ManyToManyField(tags,related_name='ringTAGS',blank=True)
    metal = models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('ring','carats'),related_name='ringMetal')
    making_charges = models.IntegerField(blank=False,null=True)
    #diamond = models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('ring','diamond'),related_name='ringDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    #gemstones=models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('ring','gemstone'),related_name='ringGemstone')
    def __str__(self):
        return self.product_type+" / "+self.product_code

    class Meta:
        verbose_name = "Ring Product"
        verbose_name_plural = "Ring Products"
        ordering=['product_code']

class braceletProduct(models.Model):#------------------------------------------------Bracelet
    product_code = models.CharField(max_length=10,null=True,blank=False,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    product_type_choice = (('Other','Other'),('Gold','Gold'),('Diamond','Diamond'),('Floral','Floral'))
    product_type = models.CharField(max_length=20,choices=product_type_choice,null=True,blank=False,default='')
    tag = models.ManyToManyField(tags,related_name='braceletTAGS',blank=True)
    metal = models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('bracelet','carats'),related_name='braceletMetal')
    making_charges = models.IntegerField(blank=False,null=True)
    #diamond=models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('bracelet','diamond'),related_name='braceletDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    #gemstones = models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('bracelet','gemstone'),related_name='braceletGemstone')
    def __str__(self):
        return self.product_type+" / "+self.product_code

    class Meta:
        verbose_name = "Bracelet Product"
        verbose_name_plural = "Bracelet Products"
        ordering=['product_code']

class nosepinProduct(models.Model):#---------------------------------------------------Nosepin
    product_code = models.CharField(max_length=10,null=True,blank=False,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    product_type_choice = (('Other','Other'),('Gold','Gold'),('Diamond','Diamond'),('Gemstone','Gemstone'))
    product_type = models.CharField(max_length=20,choices=product_type_choice,null=True,blank=False,default='')
    tag=models.ManyToManyField(tags,related_name='nosepinTAGS',blank=True)
    metal = models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('nosepin','carats'),related_name='nosepinMetal')
    making_charges = models.IntegerField(blank=False,null=True)
    #diamond=models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('nosepin','diamond'),related_name='nosepinDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    #gemstones=models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('nosepin','gemstone'),related_name='nosepinGemstone')
    def __str__(self):
        return self.productType+" / "+self.productCode
    class Meta:
        verbose_name = "Nosepin Product"
        verbose_name_plural = "Nosepin Products"
        ordering=['product_code']

class necklaceProduct(models.Model):#--------------------------------------------------Necklace
    product_code = models.CharField(max_length=10,null=True,blank=False,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    product_type_choice = (('Other','Other'),('Gold','Gold'),('Diamond','Diamond'),('Bridal','Bridal'))
    product_type = models.CharField(max_length=20,choices=product_type_choice,null=True,blank=False,default='')
    tag = models.ManyToManyField(tags,related_name='necklaceTAGS',blank=True)
    metal = models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('necklace','carats'),related_name='necklaceMetal')
    making_charges = models.IntegerField(blank=False,null=True)
    #diamond = models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('necklace','diamond'),related_name='necklaceDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    #gemstones=models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('necklace','gemstone'),related_name='necklaceGemstone')
    def __str__(self):
        return self.productType+" / "+self.productCode
    class Meta:
        verbose_name = "Necklace Product"
        verbose_name_plural = "Necklace Products"
        ordering=['product_code']

class mangalsutraProduct(models.Model):#---------------------------------------------Mangalsutra
    product_code = models.CharField(max_length=10,null=True,blank=False,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    product_type_choice = (('Other','Other'),('Gold','Gold'),('Diamond','Diamond'),('Bridal','Bridal'))
    product_type=models.CharField(max_length=20,choices=product_type_choice,null=True,blank=False,default='')
    tag = models.ManyToManyField(tags,related_name='mangalsutraTAGS',blank=True)
    metal = models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('mangalsutra','carats'),related_name='mangalsutraMetal',blank=False)
    making_charges=models.IntegerField(blank=False,null=True)
    #diamond = models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('mangalsutra','diamond'),related_name='mangalsutraDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    #gemstones=models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('mangalsutra','gemstone'),related_name='mangalsutraGemstone')
    def __str__(self):
        return self.productType+" / "+self.productCode
    class Meta:
        verbose_name = "Mangalsutra Product"
        verbose_name_plural = "Mangalsutra Products"
        ordering=['product_code']


#--------------------------------------------------X-X-X---------------------------------------------------------#



#----------------------------------------------------------------------------------------------------------------#
#---------------------------------------------Linking Models-----------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------#


class metalDetails(models.Model):#-----------------------------------------Metal Details
    earring = models.ForeignKey(earringProduct,blank=False,null=True)
    bangle = models.ForeignKey(bangleProduct,blank=True,null=True)
    ring = models.ForeignKey(ringProduct,blank=True,null=True)
    bracelet = models.ForeignKey(braceletProduct,blank=True,null=True)
    nosepin = models.ForeignKey(nosepinProduct,blank=True,null=True)
    necklace = models.ForeignKey(necklaceProduct,blank=True,null=True)
    mangalsutra = models.ForeignKey(mangalsutraProduct,blank=False,null=True)
    metal = models.ManyToManyField(METAL,blank=False)
    carats = models.ForeignKey(METALCARAT,related_name='metalCarat',blank=False,null=True)
    weight_of_metal = models.DecimalField(max_digits=8,decimal_places=5,null=True,blank=False)
    price_for_metal = models.IntegerField(blank=False,null=True)
    def __str__(self):
        return self.carats.carats


class diamondDetails(models.Model):#--------------------------------------Diamond Details
    earring = models.ForeignKey(earringProduct,blank=True,null=True)
    bangle = models.ForeignKey(bangleProduct,blank=True,null=True)
    ring = models.ForeignKey(ringProduct,blank=True,null=True)
    bracelet = models.ForeignKey(braceletProduct,blank=True,null=True)
    nosepin = models.ForeignKey(nosepinProduct,blank=True,null=True)
    necklace = models.ForeignKey(necklaceProduct,blank=True,null=True)
    mangalsutra = models.ForeignKey(mangalsutraProduct,blank=True,null=True)
    #diamond=models.ForeignKey(DIAMOND,blank=False,null=True)
    clarity_choices = (('FL','FL'),('IF','IF'),('VVS1','VVS1'),('VVS2','VVS2'),('SI1','SI1'),('SI2','SI2'),('I1','I1'),('I2','I2'),('I3','I3'))
    diamond_clarity = models.CharField(max_length=4,choices=clarity_choices,blank=True,null=True,unique=True)
    color_choices = (('DF','DF'),('GH','GH'),('IJ','IJ'),('KM','KM'),('NR','NR'),('SZ','SZ'))
    diamond_color = models.CharField(max_length=2,choices=color_choices,default='',null=True,blank=True)
    shape_choices = (('Other','Other'),('Round','Round'),('Oval','Oval'),('Pear','Pear'),('Heart','Heart'),('Princess','Princess'),('Asscher','Asscher'),('Marquise','Marquise'),('Emerald','Emerald'),('Radiant','Radiant'),('Cushion','Cushion'))
    diamond_shape = models.CharField(max_length=15,choices=shape_choices,blank=True,null=True)
    number_of_diamonds=models.IntegerField(null=True,blank=False)
    weight_of_diamonds=models.DecimalField(max_digits=8,decimal_places=5,null=True,blank=False)
    diamond_price=models.IntegerField() #------Can Keep It Here Or Not
    def __str__(self):
        return self.diamond_clarity+" / "+str(self.number_of_diamonds)+" / "+str(self.weight_of_diamonds)
    class Meta:
        verbose_name_plural = "Diamond Detail"
        verbose_name_plural = "Diamond Details"


class gemstoneDetails(models.Model):#--------------------------------------Gemstone Details
    earring = models.ForeignKey(earringProduct,blank=True,null=True)
    bangle = models.ForeignKey(bangleProduct,blank=True,null=True)
    ring = models.ForeignKey(ringProduct,blank=True,null=True)
    bracelet = models.ForeignKey(braceletProduct,blank=True,null=True)
    nosepin = models.ForeignKey(nosepinProduct,blank=True,null=True)
    necklace = models.ForeignKey(necklaceProduct,blank=True,null=True)
    mangalsutra = models.ForeignKey(mangalsutraProduct,blank=True,null=True)
    #gemstone=models.ForeignKey(GEMSTONES,blank=False,null=True)

    stone_choices=(('Emerald','Emerald'),('Ruby','Ruby'),('Amethyst','Amethyst'),('Pink Tourmaline','Pink Tourmaline'),('Garnet','Garnet'),('Citrine','Citrine'),('Pearls','Pearls'),('Blue Topaz','Blue Topaz'),('Saphire','Saphire'),('Iolite','Iolite'))
    gemstone=models.CharField(max_length=20,choices=stone_choices,null=True,blank=False,unique=True)
    shape_choices = (('Other','Other'),('Round','Round'),('Oval','Oval'),('Pear','Pear'),('Heart','Heart'),('Princess','Princess'),('Asscher','Asscher'),('Marquise','Marquise'),('Emerald','Emerald'),('Radiant','Radiant'),('Cushion','Cushion'))
    gemstone_shape = models.CharField(max_length=15,choices=shape_choices,blank=True,null=True)
    number_of_gemstones=models.IntegerField(null=True,blank=False)
    weight_of_gemstones=models.DecimalField(max_digits=8,decimal_places=5,null=True)#---------------------------Currently not included in admin site
    gemstone_price=models.IntegerField(null=True,blank=False) #------Can Keep It Here or not
    def __str__(self):
        return self.gemstone+" / "+str(self.numberOfGemstones)+" / "+str(self.weightOfGemstones)
    class Meta:
        verbose_name = "Gemstone Detail"
        verbose_name_plural = "Gemstone Details"

class PHOTOS(models.Model):
    earringPhoto=models.ForeignKey(earringProduct,related_name='earing_photo',blank=True,null=True)
    banglePhoto=models.ForeignKey(bangleProduct,related_name='bangle_photo',blank=True,null=True)
    ringPhoto=models.ForeignKey(ringProduct,related_name='ring_photo',blank=True,null=True)
    braceletPhoto=models.ForeignKey(braceletProduct,related_name='bracelet_photo',blank=True,null=True)
    nosepinPhoto=models.ForeignKey(nosepinProduct,related_name='nosepin_photo',blank=True,null=True)
    necklacePhoto=models.ForeignKey(necklaceProduct,related_name='necklace_photo',blank=True,null=True)
    mangalsutraPhoto=models.ForeignKey(mangalsutraProduct,related_name='mangalsutra_photo',blank=True,null=True)
    photo=models.ImageField(upload_to='productPhotos/',null=True,blank=True)
    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
#--------------------------------------------------X-X-X---------------------------------------------------------#
