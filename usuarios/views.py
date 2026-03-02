from django.shortcuts import render, redirect
from .models import Perfil
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import get_object_or_404

def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente")
    return redirect('login')

from .models import Perfil

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            Perfil.objects.create(
                user=user,
                nombre=user.username
            )

            return redirect('login')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})



@login_required
def lista_perfiles(request):
    perfiles = Perfil.objects.all()
    return render(request, 'lista_perfiles.html', {'perfiles': perfiles})

@login_required
def dashboard(request):
    perfil, creado = Perfil.objects.get_or_create(
        user=request.user,
        defaults={'nombre': request.user.username}
    )

    return render(request, 'dashboard.html', {'perfil': perfil})
