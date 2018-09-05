from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    cedula = models.CharField(max_length=20, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    ip_cliente = models.CharField(max_length=50, null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return '%s %s - %s' % (self.usuario.first_name, self.usuario.last_name, self.usuario.email)