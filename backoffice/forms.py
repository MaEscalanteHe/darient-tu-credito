from django import forms
from django.db.models import fields
from .models import Bank, Client, Credit

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = [
            'name', 
            'address', 
            'type'
            ]

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'birthday',
            'age',
            'nationality',
            'address',
            'email',
            'phone',
            'type',
            'bank'
        ]
        widgets = {
            'birthday': forms.DateInput(format=('%d-%m-%Y'), 
                                             attrs={'type':'date', 
                                            'placeholder':'Select a date'})
        }

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = [
            'client',
            'description',
            'minPayment',
            'maxPayment',
            'creditMonths',
            'bank',
            'type'
            ]