from django.db import models
import os
from twilio.rest import Client
# Create your models here.
class Score(models.Model):
    result=models.CharField(max_length=100)

    def __str__(self):
        return (self.result)
    
    def save(self,*args,**kwargs):
        account_sid = 'ACb5e9dca96fa78d25d75f300227ffdaa7'
        auth_token = 'e43db6bf12cbac1759d63e8351344691'
        client = Client(account_sid, auth_token)
        message= client.messages.create(
            body='hi there, order ahead '+str(self.result),
            from_='+16018951916',
            to='+917975519844')
