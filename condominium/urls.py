from django.conf.urls import include, url
from . import views

urlpatterns = [

  url(r'^$', views.condominium_index, name='condominium_index'),
  url(r'^new_or_edit$', views.condominium_new_or_edit, name='condominium_new_or_edit'),

]