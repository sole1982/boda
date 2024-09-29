from django.shortcuts import render, redirect
from .forms import FotoForm
from .models import Foto
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
def subir_foto(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('galeria')  # Redirigir a la galería tras la subida
    else:
        form = FotoForm()
    
    return render(request, 'subir_fotos.html', {'form': form})

def galeria(request):
    # Obtener todas las fotos ordenadas por fecha de subida
    fotos = Foto.objects.all().order_by('-fecha_subida')

    # Manejar el formulario de subida de fotos
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)  # Obtener los datos y archivos del formulario
        if form.is_valid():
            form.save()  # Guardar la nueva foto
            return redirect('galeria')  # Redirigir a la galería después de la subida
    else:
        form = FotoForm()

    # Renderizar la página con las fotos y el formulario
    return render(request, 'galeria.html', {'fotos': fotos, 'form': form})


@receiver(post_delete, sender=Foto)
def eliminar_imagen(sender, instance, **kwargs):
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)