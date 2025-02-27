from django.urls import path
from . import views
from .views import agregar_comentario, agregar_reaccion
urlpatterns = [
    path('subir/', views.subir_foto, name='subir_foto'),
    path('', views.galeria, name='galeria'),
    path('comentario/<int:foto_id>/', agregar_comentario, name='agregar_comentario'),
    path('reaccion/<int:foto_id>/', agregar_reaccion, name='agregar_reaccion'),
     path('ultima-foto/', views.ultima_foto, name='ultima_foto'),
    path('obtener-ultima-foto/', views.obtener_ultima_foto, name='obtener_ultima_foto'),
]

