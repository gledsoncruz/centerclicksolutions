from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('cpf', 'cel', 'dta_nasc',)
        widgets = {'dta_nasc': forms.DateInput(attrs={'class':'datepicker'})}