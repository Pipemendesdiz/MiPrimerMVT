from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random

from home.models import Familiar

def crear_familiar(request):
    
    familiar1 = Familiar(nombre='Carlota', apellido='Izuel',edad='56', fecha_de_nacimiento='1966-01-12')
    familiar1.save()
    familiar2 = Familiar(nombre='Felipe', apellido='Mendes Diz',edad='68', fecha_de_nacimiento='1954-02-20')
    familiar2.save()
    familiar3 = Familiar(nombre='India', apellido='Mendes Diz',edad='8', fecha_de_nacimiento='2014-09-16')
    familiar3.save()
    template = loader.get_template("crear_familiar.html")
    template_renderizado = template.render({'familiar1': familiar1, 'familiar2': familiar2, 'familiar3':familiar3})
    return HttpResponse(template_renderizado)
    
def ver_familiares(request):
    
    familiares = Familiar.objects.all()
    
    template = loader.get_template("ver_familiares.html")
    template_renderizado = template.render({'familiares': familiares})
    
    return HttpResponse(template_renderizado)



