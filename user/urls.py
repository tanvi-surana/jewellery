from django.conf.urls import url,include
from user.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^accounts/login-signup/$',LoginSignup,name='login_signup'),
    url(r'^accounts/get-or-create/$',GetOrCreate,name='fb_login'),
]
