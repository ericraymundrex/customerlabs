from django.db import models
from account.models import Account

class Destination(models.Model):
    account_id=models.ForeignKey(Account, on_delete=models.CASCADE,blank=False,null=False)
    destination_url=models.CharField(max_length=300)
    HTTP_methos_for_destination=models.CharField(max_length=10)


    def __str__(self):
        return self.destination_url