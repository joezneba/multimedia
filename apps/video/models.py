from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.nombre_categoria

class TipoVideo(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.nombre


class Video(models.Model):
    nombre = models.CharField(max_length=100)
    formato = models.CharField(max_length=20)
    duracion = models.TimeField()
    file = models.FileField()
    activo = models.BooleanField(default=False)
    caratula = models.ImageField(null=True, blank=True)
    fecha_estreno = models.DateField(null=True, blank=True)
    sinopsis = models.TextField(null=True, blank=True)
    tipo_video_id = models.ForeignKey(TipoVideo, on_delete=models.CASCADE, null=True, blank=True)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.nombre, self.tipo_video_id)