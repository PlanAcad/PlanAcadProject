from django import forms  

ESTADO = [
    ('IC1', 'Inicio de clases 1er cuatrimestre'),
    ('FC1', 'Fin de clases 1er cuatrimestre'),
    ('IC2', 'Inicio de clases 2do cuatrimestre'),
    ('FC2', 'Fin de clases 2do cuatrimestre'),
    ('EF', 'Examen final con suspensión de clase'),
    ('EF', 'Examen final sin suspensión de clase'),
    ('RI', 'Receso de invierno'),
    ('F', 'Feriado'),
    ('DN', 'Dia Normal')
    ]

class FechaCalendarioAcademicoUpdateForm(forms.Form):
        fecha_desde = forms.DateField(widget=forms.DateInput())
        fecha_hasta = forms.DateField(widget=forms.DateInput(),required=False)
        actividad = forms.CharField(initial='DN',max_length=2,widget=forms.Select(choices=ESTADO))
        descripcion = forms.CharField(max_length=100,widget=forms.Textarea(),required=False)
        