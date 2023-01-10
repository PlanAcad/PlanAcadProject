from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def registerView(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
        context = {
            'form': form 
        }
        return render(request,'registration/register.html', context)