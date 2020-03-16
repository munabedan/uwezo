from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Farmers
        fields=( 'farmerID','firstName','lastName','localAddress','age','phoneNumber')

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('productID','DOD','quantity','storageHygiene','bacterialScreening','fatContent')


class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payments
        fields=('paymentID','DOP','Price','farmer')