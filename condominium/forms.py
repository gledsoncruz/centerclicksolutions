from django import forms
from localflavor.br.forms import BRPhoneNumberField, BRCPFField, BRStateChoiceField, BRZipCodeField, BRCNPJField
from django.conf import settings
from .models import Customer, Condominium

class CustomerForm(forms.ModelForm):
  cel = BRPhoneNumberField()
  state = BRStateChoiceField()
  cep = BRZipCodeField()
  if settings.VALID_CPF:
    cpf = BRCPFField()

  class Meta:
    model = Customer
    fields = ('cpf', 'cel', 'dta_nasc', 'address', 'number', 'compl', 'state', 'city', 'cep', )
    widgets = {
      'dta_nasc': forms.DateInput(attrs={'class':'datepicker'}),
      }

class CondominiumForm(forms.ModelForm):
  tel = BRPhoneNumberField()
  state = BRStateChoiceField()
  cep = BRZipCodeField()
  if settings.VALID_CNPJ:
    cnpj = BRCNPJField()

  class Meta:
    model = Condominium
    fields = ('rsocial', 'cnpj', 'tel', 'address', 'number', 'compl', 'state', 'city', 'cep', )
    widgets = {
      'dta_nasc': forms.DateInput(attrs={'class':'datepicker'}),
      }


