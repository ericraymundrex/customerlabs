from .serializers import DestinationSerializers
from .models import Destination
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.models import Account


# class DestinationViewSet(viewsets.ModelViewSet):
#     queryset=Destination.objects.all()
#     serializer_class=DestinationSerializers
#     http_method_names = ['get', 'post', 'head','delete']

@api_view(['GET','POST'])
def destination_list(request):
    if request.method=='GET':
        destination=Destination.objects.all()
        serializers=DestinationSerializers(destination,many=True)
        return Response(serializers.data)

    elif request.method=='POST':
        try:
            request.headers['app-id']
            request.headers['app-sectet']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

            
        try:
            account=Account.objects.get(pk=request.headers['app-id'])
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        print("-------------")
        if str(account.app_secret_token).replace("-","")==request.headers['app-sectet']:
            request.data['account_id']=request.headers['app-id']
            serializers=DestinationSerializers(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
