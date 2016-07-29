from django.db import models

# Create your models here.

#----------------------------------------------------------------------------------------------------------------#
#--------------------------------------------Metal,Diamond,Gemstones---------------------------------------------#
#----------------------------------------------------------------------------------------------------------------#

#-------------------------------------Information About models which are linked as ManyToManyField to products using through through fields of through fields of their details
class METAL(models.Model):
    metalChoices=(('Yellow Gold','Yellow Gold'),('White Gold','White Gold'))
    metal=models.CharField(max_length=15,choices=metalChoices,null=True,blank=False,unique=True)

    def __str__(self):
        return self.metal
    
    class Meta:
        verbose_name = 'METAL'
        verbose_name_plural='METALS'
        ordering = ['-metal']

class METALCARAT(models.Model):
    caratChoices=(('14','14'),('16','16'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'))
    carats=models.CharField(max_length=2,choices=caratChoices,null=True,blank=False,unique=True)
    def __str__(self):
        return self.carats
    
    class Meta:
        verbose_name = 'CARAT'
        verbose_name_plural='CARTATS'
        ordering=['carats']


class DIAMOND(models.Model):
    clarityChoices=(('FL','FL'),('IF','IF'),('VVS1','VVS1'),('VVS2','VVS2'),('SI1','SI1'),('SI2','SI2'),('I1','I1'),('I2','I2'),('I3','I3'))
    diamondClarity=models.CharField(max_length=4,choices=clarityChoices,blank=True,null=True,unique=True)
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
    stoneChoices=(('Emerald','Emerald'),('Ruby','Ruby'),('Amethyst','Amethyst'),('Pink Tourmaline','Pink Tourmaline'),('Garnet','Garnet'),('Citrine','Citrine'),('Pearls','Pearls'),('Blue Topaz','Blue Topaz'),('Saphire','Saphire'),('Iolite','Iolite'))
    gemstone=models.CharField(max_length=20,choices=stoneChoices,null=True,blank=False,unique=True)
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
    productCode=models.CharField(max_length=10,null=True,blank=False,unique=True)
    dateAdded=models.DateTimeField(auto_now_add=True)
    productTypeChoice=(('Other','Other'),('Studs','Studs'),('Polki','Polki'),('Drops','Drops'),('Hoops','Hoops'),('Jhumki','Jhumki'),('Sui-Dhaga','Sui-Dhaga'),('Cluster','Cluster'),('Chand Bali','Chand Bali'))
    productType=models.CharField(max_length=20,choices=productTypeChoice,null=True,blank=False,default='')
    tag=models.ManyToManyField(tags,related_name='earringTAGS',blank=True)
    metal=models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('earring','carats'),related_name='earingMetal',blank=False)
    makingCharges=models.IntegerField(blank=False,null=True)
    diamond=models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('earring','diamond'),related_name='earingDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    gemstones=models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('earring','gemstone'),related_name='earingGemstone')
    def __str__(self):
        return self.productType+" / "+self.productCode
    class Meta:
        verbose_name = "Earring Product"
        verbose_name_plural = "Earring Products"
        ordering=['productCode']

class bangleProduct(models.Model):#--------------------------------------------------Bangle
    productCode=models.CharField(max_length=10,null=True,blank=False,unique=True)
    dateAdded=models.DateTimeField(auto_now_add=True)
    productTypeChoice=(('Other','Other'),('Round','Round'),('Oval','Oval'),('Gold','Gold'),('Bridal','Bridal'))
    productType=models.CharField(max_length=20,choices=productTypeChoice,null=True,blank=False,default='')
    tag=models.ManyToManyField(tags,related_name='bangleTAGS',blank=True)
    metal=models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('bangle','carats'),related_name='bangleMetal')
    makingCharges=models.IntegerField(blank=False,null=True)
    diamond=models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('bangle','diamond'),related_name='bangleDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    gemstones=models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('bangle','gemstone'),related_name='bangleGemstone')
    def __str__(self):
        return self.productType+" / "+self.productCode
    class Meta:
        verbose_name = "Bangle Product"
        verbose_name_plural = "Bangle Products"
        ordering=['productCode']

class ringProduct(models.Model):#-------------------------------------------------------Ring
    productCode=models.CharField(max_length=10,null=True,blank=False,unique=True)
    dateAdded=models.DateTimeField(auto_now_add=True)
    productTypeChoice=(('Other','Other'),('Engagement','Engagement'),('Couple Bands','Couple Bands'),('Navratna','Navratna'),('Cocktail','Cocktail'),('Platinum','Platinum'))
    productType=models.CharField(max_length=20,choices=productTypeChoice,null=True,blank=False,default='')
    tag=models.ManyToManyField(tags,related_name='ringTAGS',blank=True)
    metal=models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('ring','carats'),related_name='ringMetal')
    makingCharges=models.IntegerField(blank=False,null=True)
    diamond=models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('ring','diamond'),related_name='ringDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    gemstones=models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('ring','gemstone'),related_name='ringGemstone')
    def __str__(self):
        return self.productType+" / "+self.productCode
    class Meta:
        verbose_name = "Ring Product"
        verbose_name_plural = "Ring Products"
        ordering=['productCode']

class braceletProduct(models.Model):#------------------------------------------------Bracelet
    productCode=models.CharField(max_length=10,null=True,blank=False,unique=True)
    dateAdded=models.DateTimeField(auto_now_add=True)
    productTypeChoice=(('Other','Other'),('Gold','Gold'),('Diamond','Diamond'),('Floral','Floral'))
    productType=models.CharField(max_length=20,choices=productTypeChoice,null=True,blank=False,default='')
    tag=models.ManyToManyField(tags,related_name='braceletTAGS',blank=True)
    metal=models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('bracelet','carats'),related_name='braceletMetal')
    makingCharges=models.IntegerField(blank=False,null=True)
    diamond=models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('bracelet','diamond'),related_name='braceletDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    gemstones=models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('bracelet','gemstone'),related_name='braceletGemstone')
    def __str__(self):
        return self.productType+" / "+self.productCode
    class Meta:
        verbose_name = "Bracelet Product"
        verbose_name_plural = "Bracelet Products"
        ordering=['productCode']

class nosepinProduct(models.Model):#---------------------------------------------------Nosepin
    productCode=models.CharField(max_length=10,null=True,blank=False,unique=True)
    dateAdded=models.DateTimeField(auto_now_add=True)
    productTypeChoice=(('Other','Other'),('Gold','Gold'),('Diamond','Diamond'),('Gemstone','Gemstone'))
    productType=models.CharField(max_length=20,choices=productTypeChoice,null=True,blank=False,default='')
    tag=models.ManyToManyField(tags,related_name='nosepinTAGS',blank=True)
    metal=models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('nosepin','carats'),related_name='nosepinMetal')
    makingCharges=models.IntegerField(blank=False,null=True)
    diamond=models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('nosepin','diamond'),related_name='nosepinDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    gemstones=models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('nosepin','gemstone'),related_name='nosepinGemstone')
    def __str__(self):
        return self.productType+" / "+self.productCode
    class Meta:
        verbose_name = "Nosepin Product"
        verbose_name_plural = "Nosepin Products"
        ordering=['productCode']

class necklaceProduct(models.Model):#--------------------------------------------------Necklace
    productCode=models.CharField(max_length=10,null=True,blank=False,unique=True)
    dateAdded=models.DateTimeField(auto_now_add=True)
    productTypeChoice=(('Other','Other'),('Gold','Gold'),('Diamond','Diamond'),('Bridal','Bridal'))
    productType=models.CharField(max_length=20,choices=productTypeChoice,null=True,blank=False,default='')
    tag=models.ManyToManyField(tags,related_name='necklaceTAGS',blank=True)
    metal=models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('necklace','carats'),related_name='necklaceMetal')
    makingCharges=models.IntegerField(blank=False,null=True)
    diamond=models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('necklace','diamond'),related_name='necklaceDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    gemstones=models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('necklace','gemstone'),related_name='necklaceGemstone')
    def __str__(self):
        return self.productType+" / "+self.productCode
    class Meta:
        verbose_name = "Necklace Product"
        verbose_name_plural = "Necklace Products"
        ordering=['productCode']

class mangalsutraProduct(models.Model):#---------------------------------------------Mangalsutra
    productCode=models.CharField(max_length=10,null=True,blank=False,unique=True)
    dateAdded=models.DateTimeField(auto_now_add=True)
    productTypeChoice=(('Other','Other'),('Gold','Gold'),('Diamond','Diamond'),('Bridal','Bridal'))
    productType=models.CharField(max_length=20,choices=productTypeChoice,null=True,blank=False,default='')
    tag=models.ManyToManyField(tags,related_name='mangalsutraTAGS',blank=True)
    metal=models.ManyToManyField(METALCARAT,through='metalDetails',through_fields=('mangalsutra','carats'),related_name='mangalsutraMetal',blank=False)
    makingCharges=models.IntegerField(blank=False,null=True)
    diamond=models.ManyToManyField(DIAMOND,through='diamondDetails',through_fields=('mangalsutra','diamond'),related_name='mangalsutraDiamond')
    #diamondPrice=models.IntegerField() #------Can Keep It Here or Not
    gemstones=models.ManyToManyField(GEMSTONES,through='gemstoneDetails',through_fields=('mangalsutra','gemstone'),related_name='mangalsutraGemstone')
    def __str__(self):
        return self.productType+" / "+self.productCode
    class Meta:
        verbose_name = "Mangalsutra Product"
        verbose_name_plural = "Mangalsutra Products"
        ordering=['productCode']


#--------------------------------------------------X-X-X---------------------------------------------------------#



#----------------------------------------------------------------------------------------------------------------#
#---------------------------------------------Linking Models-----------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------#
         

class metalDetails(models.Model):#-----------------------------------------Metal Details
    earring=models.ForeignKey(earringProduct,blank=False,null=True)
    bangle=models.ForeignKey(bangleProduct,blank=True,null=True)
    ring=models.ForeignKey(ringProduct,blank=True,null=True)
    bracelet=models.ForeignKey(braceletProduct,blank=True,null=True)
    nosepin=models.ForeignKey(nosepinProduct,blank=True,null=True)
    necklace=models.ForeignKey(necklaceProduct,blank=True,null=True)
    mangalsutra=models.ForeignKey(mangalsutraProduct,blank=False,null=True)
    metal=models.ManyToManyField(METAL,blank=False)
    carats=models.ForeignKey(METALCARAT,related_name='metalCarat',blank=False,null=True)
    weightOfMetal=models.DecimalField(max_digits=8,decimal_places=5,null=True,blank=False)
    priceForMetal=models.IntegerField(blank=False,null=True)
    def __str__(self):
        return self.carats.carats
    class Meta:
        verbose_name_plural = "Metal Detail"
        verbose_name_plural = "Metal Details"



class diamondDetails(models.Model):#--------------------------------------Diamond Details
    earring=models.ForeignKey(earringProduct,blank=True,null=True)
    bangle=models.ForeignKey(bangleProduct,blank=True,null=True)
    ring=models.ForeignKey(ringProduct,blank=True,null=True)
    bracelet=models.ForeignKey(braceletProduct,blank=True,null=True)
    nosepin=models.ForeignKey(nosepinProduct,blank=True,null=True)
    necklace=models.ForeignKey(necklaceProduct,blank=True,null=True)
    mangalsutra=models.ForeignKey(mangalsutraProduct,blank=True,null=True)
    diamond=models.ForeignKey(DIAMOND,blank=False,null=True)
    colorChoices=(('DF','DF'),('GH','GH'),('IJ','IJ'),('KM','KM'),('NR','NR'),('SZ','SZ'))
    diamondColor=models.CharField(max_length=2,choices=colorChoices,default='',null=True,blank=True)
    shapeChoices=(('Other','Other'),('Round','Round'),('Oval','Oval'),('Pear','Pear'),('Heart','Heart'),('Princess','Princess'),('Asscher','Asscher'),('Marquise','Marquise'),('Emerald','Emerald'),('Radiant','Radiant'),('Cushion','Cushion'))
    diamondShape=models.CharField(max_length=15,choices=shapeChoices,blank=True,null=True)
    numberOfDiamonds=models.IntegerField(null=True,blank=False)
    weightOfDiamonds=models.DecimalField(max_digits=8,decimal_places=5,null=True,blank=False)
    diamondPrice=models.IntegerField() #------Can Keep It Here Or Not
    def __str__(self):
        if self.diamond is not None:
            return self.diamond.diamondClarity+" / "+str(self.numberOfDiamonds)+" / "+str(self.weightOfDiamonds)
    class Meta:
        verbose_name_plural = "Diamond Detail"
        verbose_name_plural = "Diamond Details"


class gemstoneDetails(models.Model):#--------------------------------------Gemstone Details
    earring=models.ForeignKey(earringProduct,blank=True,null=True)
    bangle=models.ForeignKey(bangleProduct,blank=True,null=True)
    ring=models.ForeignKey(ringProduct,blank=True,null=True)
    bracelet=models.ForeignKey(braceletProduct,blank=True,null=True)
    nosepin=models.ForeignKey(nosepinProduct,blank=True,null=True)
    necklace=models.ForeignKey(necklaceProduct,blank=True,null=True)
    mangalsutra=models.ForeignKey(mangalsutraProduct,blank=True,null=True)
    gemstone=models.ForeignKey(GEMSTONES,blank=False,null=True)
    shapeChoices=(('Other','Other'),('Round','Round'),('Oval','Oval'),('Pear','Pear'),('Heart','Heart'),('Princess','Princess'),('Asscher','Asscher'),('Marquise','Marquise'),('Emerald','Emerald'),('Radiant','Radiant'),('Cushion','Cushion'))
    gemstoneShape=models.CharField(max_length=15,choices=shapeChoices,blank=True,null=True)
    numberOfGemstones=models.IntegerField(null=True,blank=False)
    weightOfGemstones=models.DecimalField(max_digits=8,decimal_places=5,null=True)#---------------------------Currently not included in admin site
    gemstonePrice=models.IntegerField(null=True,blank=False) #------Can Keep It Here or not
    def __str__(self):
        return self.gemstone.gemstone+" / "+str(self.numberOfGemstones)+" / "+str(self.weightOfGemstones)
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
