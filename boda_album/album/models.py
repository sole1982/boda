from django.db import models



class Foto(models.Model):
    nombre_invitado = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='fotos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Foto de {self.nombre_invitado} - {self.fecha_subida}'
