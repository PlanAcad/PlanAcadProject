from django.http import  HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic


def IndexView(request):    
    return redirect('planificaciones:login_url')


def ComponentesView(request):    
    return render(request, 'componentes.html')
