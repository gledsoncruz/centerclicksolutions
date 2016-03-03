from django import forms
from localflavor.br.forms import BRPhoneNumberField, BRCPFField, BRStateChoiceField, BRZipCodeField
from django.conf import settings
from .models import Customer

class CustomerForm(forms.ModelForm):
  cel = BRPhoneNumberField()
  state = BRStateChoiceField()
  cep = BRZipCodeField()
  if settings.VALID_CPF:
    cpf = BRCPFField()

  class Meta:
    model = Customer
    fields = ('cpf', 'cel', 'dta_nasc', 'address', 'number', 'compl', 'state', 'city', 'cep', )
    widgets = {'dta_nasc': forms.DateInput(attrs={'class':'datepicker'})}