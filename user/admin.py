from django.contrib import admin
from user.models import AuthUser,UserProfile,AuthFBUser
# Register your models here.

admin.site.register(AuthUser)
admin.site.register(UserProfile)
admin.site.register(AuthFBUser)
