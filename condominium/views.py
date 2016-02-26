from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Condominium').exists(), login_url='/')
def condominium_index(request):
  return render(request, 'condominium/index.html', {})

