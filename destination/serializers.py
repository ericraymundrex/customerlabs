from attr import field
from rest_framework import serializers
from .models import Destination

class DestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Destination
        fields=['id','account_id','destination_url','HTTP_methos_for_destination']
        