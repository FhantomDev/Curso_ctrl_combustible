from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def primera_vista(request):
  return HttpResponse("Hola mundo <h1>Esto es un titulo</h1>")