from datetime import timedelta, timezone
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    phoneNumber = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now=True, editable=False,)
    updated_at = models.DateTimeField(auto_now_add=True, editable=True)

    otp_secret = models.CharField(max_length=16, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    
class GasRequest(models.Model):
    email = models.EmailField( blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    
    # request 
    title = models.CharField(max_length=500, blank=True, null=True)
    req_id = models.CharField(max_length=50, blank=True, null=True)
    discription = models.CharField(max_length=5000, blank=True, null=True)
    current_state = models.CharField(max_length=100,default='incomplete')
    submit_at = models.DateTimeField(auto_now=True, editable=False,)
    resolve_at = models.DateTimeField(auto_now_add=False, editable=True, blank=True, null=True)
    image = models.ImageField(upload_to="ImageReq")
    



