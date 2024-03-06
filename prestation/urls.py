from django.urls import path
from prestation.views import home, contato # Django conseidera a raiz logo sempre devemos passar o caminho completo
#configura cada url de aplicativos que criamos
urlpatterns = [
    #deixando urls no app prestation para que na pasta projeto que é o coração do site, apenas realizarmos o include
    path('', home), 
    path('contato/', contato),
    
]
