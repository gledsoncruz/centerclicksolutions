from django.conf.urls import include, url
from . import views

urlpatterns = [

  url(r'^$', views.order_of_service_index, name='orderservice_index'),

]