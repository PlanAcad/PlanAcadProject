from django import forms  
from planificaciones.modelos.modelAsignatura import Asignatura
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

profesor_group = Group.objects.get(name='profesor')
jefe_carrera_group = Group.objects.get(name='jefe de carrera')
queryset = User.objects.filter(groups__in=[profesor_group, jefe_carrera_group])
# queryset = queryset.filter(Q(groups=profesor_group) | Q(groups=jefe_carrera_group))

class AsignaturaForm(forms.ModelForm):
    
    profesor = forms.ModelMultipleChoiceField(
        queryset= queryset,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}))  
    class Meta:  
        model = Asignatura  
        fields = "__all__"
        labels = {
            'ano': _('Año')}