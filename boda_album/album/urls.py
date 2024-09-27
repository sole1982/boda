from django.urls import path
from . import views

urlpatterns = [
    path('subir/', views.subir_foto, name='subir_foto'),
    path('galeria/', views.galeria, name='galeria'),
]
