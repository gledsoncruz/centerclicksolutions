from django.conf.urls import include, url
from . import views

urlpatterns = [

  url(r'^$', views.condominium_index, name='condominium_index'),
  url(r'^new_or_edit$', views.customer_new_or_edit, name='customer_new_or_edit'),

]