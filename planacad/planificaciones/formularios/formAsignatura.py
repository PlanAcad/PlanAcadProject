from django import forms  
from planificaciones.modelos.modelAsignatura import Asignatura
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _

class AsignaturaForm(forms.ModelForm):
    profesor = forms.ModelMultipleChoiceField(
        queryset= User.objects.filter(groups= Group.objects.get(name='profesor')),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}))  
    class Meta:  
        model = Asignatura  
        fields = "__all__"
        labels = {
            'ano': _('Año')}