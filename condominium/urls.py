from django.conf.urls import include, url
from . import views

urlpatterns = [

  url(r'^$', views.condominium_index, name='condominium_index'),
  url(r'^customer/new_or_edit$', views.customer_new_or_edit, name='customer_new_or_edit'),
  url(r'^condominium/new$', views.condominium_new, name='condominium_new'),
  url(r'^condominium/(?P<pk>[0-9]+)/edit/$', views.condominium_edit, name='condominium_edit'),
  url(r'^condominium/list$', views.condominium_list, name='condominium_list'),

]