from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from apps.usuario import forms as forms
from apps.usuario import models as mod

# Create your views here.
''' Registro de usuarios'''
def registro(request):
    ctx = {}
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = forms.RegistroForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')

        else:
            form = forms.RegistroForm()
            return render(request, 'registration/registro.html', {'form': form})

    ctx['form'] = form
    return render(request, 'registration/registro.html', ctx)

''' Función para comprobar si el usuario posee un perfil '''
def comprobarPerfil(request):
    user = request.user
    perfil = mod.Perfil.objects.get(usuario=user)

    if perfil.cedula == None:
        data = False
    else:
        data = True
    return HttpResponse(data)

''' Función para crear un perfil de usuario '''
def crearPerfil(request):
    cedula = request.POST.get('cedula')
    telefono = request.POST.get('telefono')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    ip_cliente = request.POST.get('ip_cliente')

    perfil = mod.Perfil.objects.get(usuario_id=request.user.pk)
    perfil.cedula = cedula
    perfil.telefono = telefono
    perfil.fecha_nacimiento = fecha_nacimiento
    perfil.ip_cliente = ip_cliente

    perfil.save()
    return HttpResponse(True)