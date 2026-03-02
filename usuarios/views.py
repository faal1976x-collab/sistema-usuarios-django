from django.shortcuts import render
from .models import Perfil
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def lista_perfiles(request):
    perfiles = Perfil.objects.all()
    return render(request, 'lista_perfiles.html', {'perfiles': perfiles})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')