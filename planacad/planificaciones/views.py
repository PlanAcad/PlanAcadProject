from django.http import  HttpResponseRedirect

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def IndexView(request):    
    return render(request, 'index.html')


def LoginView(request):    
    return render(request, 'login.html')