from django.db import models
from django.utils.timezone import now


class Foto(models.Model):
    nombre_invitado = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='fotos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Foto de {self.nombre_invitado} - {self.fecha_subida}'

class Comentario(models.Model):
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE, related_name="comentarios")
    nombre = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField(default=now)

    def __str__(self):
        return f'Comentario de {self.nombre} en {self.foto}'

class Reaccion(models.Model):
    TIPOS_REACCION = [
        ('like', 'Me gusta'),
        ('love', 'Me encanta'),
        ('laugh', 'Me divierte'),
    ]
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE, related_name="reacciones")
    tipo = models.CharField(max_length=10, choices=TIPOS_REACCION)
    usuario = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.usuario} reaccionó con {self.get_tipo_display()}'