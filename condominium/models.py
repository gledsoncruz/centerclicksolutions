from __future__ import unicode_literals
from django.contrib.auth.models import User
from datetime import date
from django.db import models

# Create your models here.

class Customer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  cpf = models.CharField(max_length=15, unique=True)
  cel = models.CharField(max_length=15)
  dta_nasc = models.DateField(default=date.today)
  address = models.CharField(max_length=80, default='')
  number = models.CharField(max_length=5, default='')
  compl = models.CharField(max_length=50, blank=True)
  state = models.CharField(max_length=50, default='')
  city = models.CharField(max_length=80, default='')
  cep = models.CharField(max_length=10, default='')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return self.user.email
