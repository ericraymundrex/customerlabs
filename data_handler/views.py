from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.models import Account
from destination.models import Destination

import requests

@api_view(['POST'])
def datahandler(request):
    # Finding the secret token
    try:
        app_secret_token=request.headers['cl-x-token']
    except:
        Response(status=status.HTTP_400_BAD_REQUEST)
    
    account=Account.objects.get(app_secret_token=app_secret_token)
    destinations=Destination.objects.all().filter(account_id=account.account_id)
    payload=request.data
    for d in destinations:
        if d.HTTP_methos_for_destination=="GET":
            r=requests.get('https://'+str(d),params=payload)
            print(r.text)
            # print(r.status_code)
            # print(r.ok)
            # print(r.headers)
        elif d.HTTP_methos_for_destination=="POST":
            r=requests.post('https://'+str(d),data=payload)
            r_dict=r.json()
        elif d.HTTP_methos_for_destination=="PUT":
            r=requests.put('http://'+str(d),data=payload)
            pass
    