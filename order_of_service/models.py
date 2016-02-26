from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
  name = models.CharField(max_length=80)
  cpf = models.CharField(max_length=15)
  email = models.EmailField(max_length=80)
  cel = models.CharField(max_length=15)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return self.name
