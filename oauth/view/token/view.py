from django.http import HttpResponse, Http404,JsonResponse
from oauth.models import OAuthClient, OAuthCode,OAuthToken
from time import time
from random import sample
from django.views.decorators.csrf import csrf_exempt


def code(Pdata):
    try:
        OAuthClient.objects.get(client=Pdata["client_id"], secret=Pdata["client_secret"])
        result = OAuthCode.objects.get(ClientId=Pdata["client_id"],url=Pdata["redirect_uri"],code=Pdata["code"])
        nowtime = int(time())
        if  nowtime - int(result.time) > 600:
            result.delete()
            return JsonResponse({"error":"-1","error_description":"timeout!"})


        access_token = ''.join(sample("1234567890qwertyuioADFGHJKLzxcNWEUalkdfj", 16))
        refresh_token = ''.join(sample("1234567890qwertyuioADFGHJKLzxcNWEUalkdfj", 16))
        token = OAuthToken()
        token.time = nowtime
        token.access = access_token
        token.refresh = refresh_token
        token.client = Pdata["client_id"]
        token.save()
        result.delete()
        return JsonResponse({"access_token": access_token,"refresh_token": refresh_token,"expires_in": 3600 * 48})

    except Exception as e:
        print(e)
        return JsonResponse({"error": "-2", "error_description": "code invalid!"})

def refresh(Pdata):
    try:
        OAuthClient.objects.get(client=Pdata["client_id"], secret=Pdata["client_secret"])
        result = OAuthToken.objects.get(refresh=Pdata["refresh_token"])
        result.access = ''.join(sample("1234567890qwertyuioADFGHJKLzxcNWEUalkdfj", 16))
        nowtime = int(time())
        result.time = nowtime
        result.save()
        return JsonResponse({"access_token": result.access, "refresh_token": Pdata["refresh_token"], "expires_in": 3600 * 48})

    except:
        return JsonResponse({"error": "-3", "error_description": "refresh_token invalid!"})

@csrf_exempt
def GetToken(request):
    if request.method == "POST":
        Pdata = request.POST
        if Pdata["grant_type"] == "authorization_code":
            return code(Pdata)
        elif Pdata["grant_type"] == "refresh_token":
            return refresh(Pdata)
    else:
        HttpResponse("Unknown")