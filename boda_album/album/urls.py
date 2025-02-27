from django.urls import path
from . import views
from .views import agregar_comentario, agregar_reaccion, eliminar_foto
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('subir/', views.subir_foto, name='subir_foto'),
    path('', views.galeria, name='galeria'),
    path('comentario/<int:foto_id>/', agregar_comentario, name='agregar_comentario'),
    path('reaccion/<int:foto_id>/', agregar_reaccion, name='agregar_reaccion'),
     path('ultima-foto/', views.ultima_foto, name='ultima_foto'),
    path('obtener-ultima-foto/', views.obtener_ultima_foto, name='obtener_ultima_foto'),
   path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
path('eliminar-foto/<int:foto_id>/', eliminar_foto, name='eliminar_foto'),


]

