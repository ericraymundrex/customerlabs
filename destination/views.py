from .serializers import DestinationSerializers
from .models import Destination
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.models import Account
from rest_framework import generics

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
            account_id=request.headers['app-id']
            app_secret_token=request.headers['app-sectet']
        except:
            return Response([{"message":"Add proper header"}],status=status.HTTP_400_BAD_REQUEST)
            
        try:
            account=Account.objects.get(pk=account_id)
        except Account.DoesNotExist:
            return Response([{"message":"Account Not found"}],status=status.HTTP_404_NOT_FOUND)
        except:
            return Response([{"message":"Enter proper secret key"}],status=status.HTTP_401_UNAUTHORIZED)
            
        if str(account.app_secret_token)==app_secret_token and str(account.account_id)==account_id:
            request.data['account_id']=account_id
            serializers=DestinationSerializers(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response([{"message":"Enter proper secret key"}],status=status.HTTP_401_UNAUTHORIZED)


class DestinationList(generics.RetrieveDestroyAPIView):
    queryset=Destination.objects.all()
    serializer_class = DestinationSerializers