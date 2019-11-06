#!coding=utf-8
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from oauth.models import OAuthToken

@csrf_exempt
def api(request):
    #tmp = {"header":{"namespace":"AliGenie.Iot.Device.Discovery","name":"DiscoveryDevices","messageId":"1bd5d003-31b9-476f-ad03-71d471922820","payLoadVersion":1 },"payload":{"accessToken":"access token"}}
    tmp = {"header":{"namespace":"AliGenie.Iot.Device.Control","name":"TurnOn","messageId":"1bd5d003-31b9-476f-ad03-71d471922820","payLoadVersion":1},"payload":{"accessToken":"AHG7ui52Wl0tqz3K","deviceId":"02646594","deviceType":"light","attribute":"powerstate","value":"on","extensions":{"extension1":"","extension2":""}}}
    # Body = eval(str(request.body.decode()))
    Body = tmp
    print(Body)

    # try:
    #     token = OAuthToken.objects.get(access=Body["payload"]["accessToken"])
    # except:
    #     return JsonResponse({"error": "-3", "error_description": "token error!"})
    # from time import time
    # if (int(time()) - token.time) > 3600 * 48:
    #     return JsonResponse({"error": "-4", "error_description": "token timeout!"})

    if Body["header"]["namespace"] == "AliGenie.Iot.Device.Discovery":
        Body["header"]["name"] = "DiscoveryDevicesResponse"

        from iMrX.models import IotDeviceType,IotDevice

        IotDeviceList = IotDevice.objects.all()
        deviceList = []
        for IotDevice in IotDeviceList:
            type = IotDeviceType.objects.get(id=IotDevice.type)
            device = {"deviceId": IotDevice.deviceid,"deviceName": IotDevice.name,"deviceType": IotDevice.typealias,"icon": type.icon,"properties": eval(type.properties),"actions": eval(type.actions)}
            from iMrX.setting import AdditionalArgs
            device = dict(device, **AdditionalArgs)
            deviceList.append(device)

        Body["payload"] = {"devices":deviceList}
        print(Body)
        return JsonResponse(Body)

    elif Body["header"]["namespace"] == "AliGenie.Iot.Device.Control":
        from iMrX.models import IotDevice
        from iMrX.views import client

        sid = Body["payload"]["deviceId"]
        state = Body["payload"]["value"]
        Body["header"]["name"] = Body["header"]["name"] + "Response"
        try:
            device = IotDevice.objects.get(deviceid=sid)
            client.publish(device.CmdTopic,state)
            payload = {"deviceId":sid}
        except:
            payload = {"deviceId":sid,"errorCode":"DEVICE_NOT_SUPPORT_FUNCTION","message":"device not support"}
        Body["payload"] = payload
        return JsonResponse(Body)
