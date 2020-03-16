from django.db import models

# Create your models here.

class Farmers(models.Model):
    farmerID=models.AutoField(primary_key=True)
    firstName=models.CharField(max_length=100,blank=False)
    lastName=models.CharField(max_length=100,blank=False)
    localAddress=models.CharField(max_length=100,blank=False)
    age=models.IntegerField()
    phoneNumber=models.IntegerField()

class Product(models.Model):
    choices=(
        ('1','PASS'),
        ('0','FAIL'),
    )
    productID= models.AutoField(primary_key=True)
    DOD=models.DateField() 
    quantity=models.IntegerField()
    storageHygiene=models.CharField(max_length=10,choices=choices)
    bacterialScreening=models.CharField(max_length=10,choices=choices)
    fatContent=models.IntegerField()
   
class Payments(models.Model):
    paymentID=models.AutoField(primary_key=True)
    DOP=models.DateField() 
    Price=models.IntegerField()
    farmer= models.ForeignKey(Farmers)
   