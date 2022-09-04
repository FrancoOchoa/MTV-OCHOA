from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def familiar_1(request):
    familiar_1=Familiar(nombre='Pablo', apellido='Ochoa', fecha_nacimiento='1963-05-05')
    familiar_1.save()
    familiar_01={'nombre':familiar_1.nombre, 'apellido':familiar_1.apellido, 'fecha_nacimiento':familiar_1.fecha_nacimiento}
    #cargo template
    plantilla=loader.get_template('familiar.html')
    #renderizo contexto (que es un diccionario)
    documento=plantilla.render(familiar_01)
    return HttpResponse(documento)

def familiar_2(request):
    familiar_2=Familiar(nombre='Cristian', apellido='Ochoa', fecha_nacimiento='1995-10-23')
    familiar_2.save()
    familiar_02={'nombre':familiar_2.nombre, 'apellido':familiar_2.apellido, 'fecha_nacimiento':familiar_2.fecha_nacimiento}
    plantilla=loader.get_template('familiar.html')
    documento=plantilla.render(familiar_02)
    return HttpResponse(documento)

def familiar_3(request):
    familiar_3=Familiar(nombre='Lucas', apellido='Ochoa', fecha_nacimiento='2002-4-12')
    familiar_3.save()
    familiar_03={'nombre':familiar_3.nombre, 'apellido':familiar_3.apellido, 'fecha_nacimiento':familiar_3.fecha_nacimiento}
    plantilla=loader.get_template('familiar.html')
    documento=plantilla.render(familiar_03)
    return HttpResponse(documento)
    


    
