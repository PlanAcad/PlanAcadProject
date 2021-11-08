from django import forms  
from planificaciones.modelos.modelPropuestaDesarrollo import PropuestaDesarrollo

class PropuestaDesarrolloForm(forms.ModelForm):  

    class Meta:  
        model = PropuestaDesarrollo  
        exclude = ['planificacion']