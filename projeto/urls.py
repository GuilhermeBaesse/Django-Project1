"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include;

urlpatterns = [
    #path('admin/', admin.site.urls), 
    path('',include('prestation.urls')), #no include voce indica o caminho do arquivo, no caso prestation tem urls e voce consegue criar os apps
    #dentro de prestation, deixar suas respectivas urls lá, e aqui só dar o include delas para evitar duplicação de codigo nessa 
    # pasta que é o coração do projeto, o path vazio '' indica a pasta raiz
    #path('prestation/',include('prestation.urls')) #Faz com que fique dominio.com/prestation/
]
