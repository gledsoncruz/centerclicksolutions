from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .forms import CustomerForm
from .models import Customer


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Condominium').exists(), login_url='/')
def condominium_index(request):
  form = CustomerForm()
  return render(request, 'condominium/index.html', {'form': form})

@login_required(login_url='/account/login/')
def customer_new_or_edit(request):
  current_user = request.user
  try:
    customer = Customer.objects.get(user=current_user)
    if request.method == "POST":
      form = CustomerForm(request.POST, instance=customer)
      if form.is_valid():
        customer = form.save()
        messages.success(request, 'Dados pessoais atualizados')
        return redirect('customer_new_or_edit')
    else:
      form = CustomerForm(instance=customer)
    return render(request, 'condominium/customer_edit.html', {'form': form})
  except ObjectDoesNotExist:
    if request.method == "POST":
      form = CustomerForm(request.POST)
      if form.is_valid():
        customer = form.save(commit=False)
        customer.user = current_user
        customer.save()
        messages.success(request, 'Dados pessoais atualizados')
        return redirect('customer_new_or_edit')
    else:
      form = CustomerForm()
    return render(request, 'condominium/customer_edit.html', {'form': form})



