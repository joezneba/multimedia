from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.usuario import models as mod

class RegistroForm(forms.Form):
    email = forms.EmailField(required=True, label='Correo Electrónico')
    first_name = forms.CharField(required=True, label='Nombres')
    last_name = forms.CharField(required=True, label='Apellidos')
    password1 = forms.CharField(required=True, label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, label='Repetir Contraseña', widget=forms.PasswordInput())
    ip_registro = forms.CharField(label='ip_registro', widget=forms.HiddenInput())

    def clean(self):
        clean_data = super(RegistroForm, self).clean()
        pass1 = clean_data.get('password1')
        pass2 = clean_data.get('password2')
        correo = clean_data.get('email')

        var = User.objects.filter(email=correo)

        if len(var) >0:
            error = forms.ValidationError(('Ya existe otro usuario con ese correo'),)
            self.add_error('email', error)

        if pass1 != pass2:
            error = forms.ValidationError(('Las contraseñas no son iguales'),)
            self.add_error('password2', error)

    def save(self):
        datos = self.cleaned_data
        ctx = {}

        for i in datos:
            ctx[i] = datos[i]

        user = User.objects.create_user(
            username = datos['email'],
            first_name = datos['first_name'],
            last_name = datos['last_name'],
            password = datos['password1'],
            email = datos['email'],
            is_active = False
        )
        user.save()
        usuario = User.objects.get(username=datos['email'])
        perfil = mod.Perfil(usuario_id=usuario.pk, ip_cliente=datos['ip_registro'])
        perfil.save()


