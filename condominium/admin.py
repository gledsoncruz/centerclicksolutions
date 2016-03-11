from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

from .models import Customer, Condominium, Plan

class CustomerInline(admin.StackedInline):
  model = Customer
  can_delete = False
  verbose_name_plural = 'customers'

class UserAdmin(BaseUserAdmin):
  inlines = (CustomerInline, )

class CondominiumAdmin(admin.ModelAdmin):
  list_display = ['rsocial', 'cnpj', 'tel', 'state',]
  search_fields = ['rsocial',]

class PlanAdmin(admin.ModelAdmin):
  list_display = ['desc', 'price', 'condominium_count',]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Condominium, CondominiumAdmin)
admin.site.register(Plan, PlanAdmin)


