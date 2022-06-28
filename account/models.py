from django.db import models
import uuid
# Create your models here.
class Account(models.Model):
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email_id=models.EmailField(max_length=50,unique=True)
    account_name=models.CharField(max_length=50)
    app_secret_token = models.UUIDField(default=uuid.uuid4, editable=False) 
    website=models.CharField(max_length=50)

    def __str__(self):
        return self.email_id