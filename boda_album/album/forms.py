from django import forms
from .models import Foto, Comentario, Reaccion

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['nombre_invitado', 'imagen']
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'texto']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'texto': forms.Textarea(attrs={'placeholder': 'Escribe un comentario...'}),
        }

class ReaccionForm(forms.ModelForm):
    class Meta:
        model = Reaccion
        fields = ['tipo']
        widgets = {
            'tipo': forms.RadioSelect(choices=Reaccion.TIPOS_REACCION),
        }
