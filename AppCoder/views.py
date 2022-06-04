from http.client import HTTPResponse
from django.shortcuts import render
from .models import curso
# Create your views here.

def curso(self):
    curso1= curso(" desarrollo web", "camada = 1525")
    curso1.save()
    documento= f'curso {curso1.nombre} - Camada: {curso1.camada}'

    return HTTPResponse(documento)

