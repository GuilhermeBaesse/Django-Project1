from django.shortcuts import render #render tem a funça de ler e renderizar o arquivo ao inves de codar o html dentro do httprepsonse
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse(request, 'home.html') #assim a gente passa o arquivo html, ou seja renderiza um templeta home.html

def contato(request):
    return HttpResponse('contato')