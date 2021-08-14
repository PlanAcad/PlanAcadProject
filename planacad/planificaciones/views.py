from django.http import  HttpResponseRedirect
# Para usar los objetos de Request y datetime
from django.http import  HttpRequest
import datetime
####

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
## import model
from .models import Asignatura
##
def IndexView(request):    
    return render(request, 'index.html')
    
##Define request    
def asignatura(request): 
   assert isinstance(request, HttpRequest) 

   # Retrieve all contacts in the database table
   asignatura_list = Asignatura.objects.order_by('nombreMateria') 

   return render(
      request, 
      'app/asignaturas.html', 
      {
         'contact_list': asignatura_list, # Embed data into the HttpResponse object
      }
   )