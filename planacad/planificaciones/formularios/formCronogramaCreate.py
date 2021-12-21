from django import forms  

DIAS = [
    ('L', 'Lunes'),
    ('M', 'Martes'),
    ('MI', 'Miercoles'),
    ('J', 'Jueves'),
    ('V', 'Viernes')
    ('S', 'Sabado')
    
    ]

class CronogramaCreateForm(forms.Form):
        dias = forms.CheckboxSelectMultiple(initial='L',max_length=2,widget=forms.Select(choices=DIAS))
        