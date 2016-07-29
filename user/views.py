from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.conf import settings
from user.verifications import VerifyFbClientAccessToken
from django.contrib.auth import login,logout,authenticate

from user.models import AuthFBUser,AuthUser
# Create your views here.

def LoginSignup(request):
    print(request.is_ajax())
    return render(request,'login-signup/login-signup.html',{})

@csrf_protect
def GetOrCreate(request):
    user_id = request.GET.get('userID')
    access_token = request.GET.get('accessToken')
    signed_request = request.GET.get('signedRequest')
    expires_in = request.GET.get('expiresIn')

    verification_response = VerifyFbClientAccessToken(access_token)
    print(verification_response)
    if verification_response == True:
        fb_user = AuthFBUser.objects.filter(user_key_id=user_id)
        if len(fb_user) is not 0:
            user_f = fb_user[0].user
            user_f.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,user_f)
        else:
            a_u = AuthUser.objects.create(username=signed_request[45:55]) #----Make It Better ... Curse Django :(
            a_u.save()
            f_a_u = AuthFBUser.objects.create(user_key_id=user_id,access_token=access_token,signed_request=signed_request,expires_in=expires_in,user=a_u)
            f_a_u.save()
            f_a_u.times_logged_in = f_a_u.times_logged_in+1
            f_a_u.verified_primary_email = True
            f_a_u.save()
            a_u.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,a_u)

    return HttpResponse('f')
