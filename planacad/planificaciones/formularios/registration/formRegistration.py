from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Group
from django import forms

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    groups = forms.ModelChoiceField(queryset= Group.objects.all())
    
    class Meta:  
        model = User  
        fields = ['username','first_name','last_name', 'email','groups', 'password1', 'password2']