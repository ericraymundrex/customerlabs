from .serializers import AccountSerializer
from .models import Account
from rest_framework import viewsets

class AccountViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    http_method_names = ['get', 'post', 'head','delete']