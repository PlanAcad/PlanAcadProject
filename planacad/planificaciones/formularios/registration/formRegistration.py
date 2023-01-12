from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from planificaciones.modelos.modelCarrera import Carrera
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django import forms

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    groups = forms.ModelChoiceField(queryset= Group.objects.all(), label="Rol")
    carrera = forms.ModelChoiceField(queryset= Carrera.objects.all())
    password1 = forms.CharField(
        label="Contraseña",
    strip=False,
    widget=forms.PasswordInput,
    help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Repetir Contraseña",
    strip=False,
    widget=forms.PasswordInput,
    help_text=password_validation.password_validators_help_text_html(),
    )
    
    class Meta:  
        model = User  
        fields = ['username','first_name','last_name', 'email','groups','carrera', 'password1', 'password2']
        labels = {
            'username': _('Nombre de Usuario'),
            'first_name': _('Nombre/s'),
            'last_name': _('Apellido/s'),
            'groups': _('Rol'),
            'password1': _('Contraseña'),
            'password2': _('Repetir Contraseña'),
            
        }