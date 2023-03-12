from django import forms

class CambiarContraseñaForm(forms.Form):
    nueva_contraseña = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)