# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .forms import CustomerForm, CondominiumForm
from .models import Customer, Condominium
from django.conf import settings

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
    return render(request, 'condominium/customer/customer_edit.html', {'form': form})
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
    return render(request, 'condominium/customer/customer_edit.html', {'form': form})

'''
CONDOMINIUM
'''


@login_required(login_url='/account/login/')
def condominium_new(request):
  if request.method == "POST":
    form = CondominiumForm(request.POST)
    if form.is_valid():
      cond = form.save(commit=False)
      cond.user = request.user
      cond.save()
      messages.success(request, 'Dados inseridos com sucesso')
      return redirect('condominium_list')
  else:
    form = CondominiumForm()
  return render(request, 'condominium/condominium/condominium_new.html', {'form': form})

@login_required(login_url='/account/login/')
def condominium_list(request):
  cond_list = Condominium.objects.filter(user=request.user)
  paginator = Paginator(cond_list, 15)
  page = request.GET.get('page')
  try:
    condominiums = paginator.page(page)
  except PageNotAnInteger:
    condominiums = paginator.page(1)
  except EmptyPage:
    condominiums = paginator.page(paginator.num_pages)
  return render(request, 'condominium/condominium/condominium_list.html', {'condominiums': condominiums})



