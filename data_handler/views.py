
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.models import Account
from destination.models import Destination

import requests

@api_view(['POST'])
def datahandler(request):
    response=[]
    try:
        app_secret_token=request.headers['cl-x-token']
    except:
        Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        account=Account.objects.get(app_secret_token=app_secret_token)
        destinations=Destination.objects.all().filter(account_id=account.account_id)
    except:
        return Response([{"message":"Enter proper secret key"}],status=status.HTTP_401_UNAUTHORIZED)
    payload=request.data

    for data in destinations:
        if data.HTTP_methos_for_destination=="GET":
            r=requests.get('https://'+str(data),params=payload)
            response.append(
                {
                    "End-Point":str(data),
                    "status":r.status_code,
                    "ok":r.ok
                }
            )
        elif data.HTTP_methos_for_destination=="POST":
            r=requests.post('https://'+str(data),data=payload)
            r_dict=r.json()
            response.append(
                {
                    "End-Point":str(data),
                    "status":r.status_code,
                    "ok":r.ok,
                    "result":r_dict
                }
            )
        elif data.HTTP_methos_for_destination=="PUT":
            r=requests.put('http://'+str(data),data=payload)
            r_dict=r.json()
            response.append(
                {
                    "End-Point":str(data),
                    "status":r.status_code,
                    "ok":r.ok,
                    "result":r_dict
                }
            )
    return Response(response,status=status.HTTP_200_OK)