from django.shortcuts import render

def order_of_service_index(request):
  return render(request, 'order_of_service/index.html', {})