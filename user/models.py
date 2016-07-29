from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

class AuthUser(AbstractUser):#---------------------Deriving User Model For Future If ever necessary to add new fields

    def get_full_name(self):
        return self.first_name+ " "+self.last_name

    def __str__(self):
        return "@%s"%super(AuthUser,self).__str__()


class UserProfile(models.Model):#-------------------Profile Of User
    user = models.OneToOneField(AuthUser,blank=False,related_name='user_profile')
    times_logged_in = models.IntegerField(default=0)
    verified_primary_email = models.BooleanField(default=False)

    def __str__(self):
        return "%s's Profile"%self.user.__str__()

class AuthFBUser(UserProfile):#---------------------Deriving From UserProfie so as to make those field available
    user_key_id = models.BigIntegerField(blank=False,null=True)
    access_token = models.CharField(max_length=400,blank=False,null=True)
    signed_request = models.CharField(max_length=500,blank=False,null=True)
    expires_in = models.IntegerField(blank=False)

#---------------------------------------------------------------------------------#
#-------------------------------- Info Models ------------------------------------#
#---------------------------------------------------------------------------------#

class PhoneNumber(models.Model):
    person = models.ForeignKey(UserProfile,blank=False,related_name='user_profile_PhoneNumber')
    phone_number = PhoneNumberField()
    def __str__(self):
    	return "@%s's phone_number"%self.person.user.__str__()

class Email(models.Model):
    person = models.ForeignKey(UserProfile,related_name='user_profile_email')
    email_id = models.EmailField(blank=False,null=True,unique=True)
    verified = models.BooleanField(default=False)
    primary = models.BooleanField(default=False)
    def __str__(self):
        return "@%s's email"%self.person.user.__str__()

class Location(models.Model):
    person = models.ForeignKey(UserProfile,related_name='user_location')
    country = models.CharField(max_length=50,blank=False,null=True)
    state = models.CharField(max_length=50,blank=False,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    hometown = models.BooleanField(default=False)
    current = models.BooleanField(default=False)

    def __str__(self):
        return "@%s's locaton"%self.person.user.__str__()

#---------------------------------------------------------------------------------#
#----------------------------------X-X-X------------------------------------------#
#---------------------------------------------------------------------------------#
