from django.conf.urls import include, url
from . import views

urlpatterns = [

  url(r'^$', views.condominium_index, name='condominium_index'),

]