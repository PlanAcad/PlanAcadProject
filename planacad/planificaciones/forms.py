from django import forms  
from .models import Asignatura

class AsignaturaForm(forms.ModelForm):  
    class Meta:  
        model = Asignatura  
        fields = "__all__"