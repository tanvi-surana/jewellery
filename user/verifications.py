#--- verifications of access tokens etc ---#
from django.conf import settings
import requests

def GetFbAppAccessToken():
    payload = {'client_id':settings.AUTH_FB_APP_ID,'client_secret':settings.AUTH_FB_APP_SECRET,'grant_type':'client_credentials'}
    checkUrl = "https://graph.facebook.com/oauth/access_token"

    r = requests.get(checkUrl,params=payload)
    if r.status_code is 200:
        text = r.text
        text = text.split('=')

        if len(text) is 2 and text[0] == 'access_token':
            return text[1]
        else:
            return "Error : Wrong Response By Fb"
    else:
        return "Error : Check Code"

def VerifyFbClientAccessToken(access_token):
    payload = {'input_token':access_token,'access_token':GetFbAppAccessToken()}
    checkUrl = "https://graph.facebook.com/debug_token"

    r = requests.get(checkUrl,params=payload)
    
    if r.status_code is 200:
        json_response = r.json()
        if json_response['data']['is_valid'] == True:
            return True
        else:
            return False
    else:
        return "Error : Check Code"
