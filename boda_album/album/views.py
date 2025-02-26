from django.shortcuts import render, redirect,get_object_or_404
from .forms import FotoForm, ComentarioForm, ReaccionForm
from .models import Foto
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from django.http import JsonResponse
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
    for foto in fotos:
        foto.likes = foto.reacciones.filter(tipo='like').count()
        foto.loves = foto.reacciones.filter(tipo='love').count()
        foto.laughs = foto.reacciones.filter(tipo='laugh').count()
    # Renderizar la página con las fotos y el formulario
    return render(request, 'galeria.html', {'fotos': fotos, 'form': form,'form_comentario': ComentarioForm(),
        'form_reaccion': ReaccionForm(), })


@receiver(post_delete, sender=Foto)
def eliminar_imagen(sender, instance, **kwargs):
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)

def agregar_comentario(request, foto_id):
    foto = get_object_or_404(Foto, id=foto_id)

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.foto = foto
            comentario.save()
            return redirect('galeria')

    return redirect('galeria')

def agregar_reaccion(request, foto_id):
    foto = get_object_or_404(Foto, id=foto_id)

    if request.method == "POST":
        form = ReaccionForm(request.POST)
        if form.is_valid():
            reaccion = form.save(commit=False)
            reaccion.foto = foto
            reaccion.usuario = "Invitado"  # Puedes cambiar esto para identificar al usuario real
            reaccion.save()
            return redirect('galeria')

    return redirect('galeria')

def ultima_foto(request):
    ultima_foto = Foto.objects.last()  # Obtiene la última foto subida
    return render(request, 'ultima_foto.html', {'ultima_foto': ultima_foto})


def obtener_ultima_foto(request):
    fotos = Foto.objects.order_by('-id')[:5]  # Últimas 5 fotos
    urls = [foto.imagen.url for foto in fotos]
    return JsonResponse({'urls': urls})