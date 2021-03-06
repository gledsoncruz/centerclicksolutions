# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from datetime import date
from django.db import models

# Create your models here.

class Plan(models.Model):
  desc = models.CharField(max_length=50)
  sigla = models.CharField(max_length=10)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  condominium_count = models.IntegerField(default=1)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "Plano"

  def __unicode__(self):
    return self.desc +" -------- "+str(self.price)

class Customer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
  cpf = models.CharField(max_length=15, unique=True)
  cel = models.CharField(max_length=15)
  dta_nasc = models.DateField(default=date.today)
  address = models.CharField(max_length=80, default='')
  number = models.CharField(max_length=5, default='')
  compl = models.CharField(max_length=50, blank=True, default='')
  state = models.CharField(max_length=50, default='')
  city = models.CharField(max_length=80, default='')
  cep = models.CharField(max_length=10, default='')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "Dados Pessoais"

  def __unicode__(self):
    return self.user.email


class Condominium(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rsocial = models.CharField(max_length=80)
  cnpj = models.CharField(max_length=20, unique=True)
  tel = models.CharField(max_length=15)
  address = models.CharField(max_length=80)
  number = models.CharField(max_length=5, blank=True)
  compl = models.CharField(max_length=50, blank=True)
  state = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  cep = models.CharField(max_length=10)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "Condominio"
    verbose_name_plural = "Condominios"

  def __unicode__(self):
    return self.rsocial
