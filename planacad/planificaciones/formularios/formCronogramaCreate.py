from django import forms  

DIAS = [
    ('L', 'Lunes'),
    ('M', 'Martes'),
    ('MI', 'Miercoles'),
    ('J', 'Jueves'),
    ('V', 'Viernes'),
    ('S', 'Sabado')
    
]

class CronogramaCreateForm(forms.Form):
        dias = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=DIAS,
            )
        