from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15,blank=True,null=True)
    company=models.CharField(max_length=100,null=True,blank=True)
    help=models.TextField(blank=True,null=True)
