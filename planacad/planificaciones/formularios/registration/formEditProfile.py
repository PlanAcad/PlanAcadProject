from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User, Group
from planificaciones.modelos.modelCarrera import Carrera
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django import forms

class EditUserForm(UserChangeForm):
    email = forms.EmailField()
    groups = forms.ModelChoiceField(queryset= Group.objects.all(), label="Rol")
    carrera = forms.ModelChoiceField(queryset= Carrera.objects.all())
    
    
    class Meta:  
        model = User  
        fields = ['username','first_name','last_name', 'email','groups','carrera']
        labels = {
            'username': _('Nombre de Usuario'),
            'first_name': _('Nombre/s'),
            'last_name': _('Apellido/s'),
            'groups': _('Rol')
            
        }