from django import forms  

DIAS = [
    ('L', 'Lunes'),
    ('M', 'Martes'),
    ('MI', 'Miércoles'),
    ('J', 'Jueves'),
    ('V', 'Viernes'),
    ('S', 'Sábado')
    
]

class CronogramaCreateForm(forms.Form):
        dias = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=DIAS,
            )
        