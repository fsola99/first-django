from django.urls import path
from inicio.views import inicio, paletas

urlpatterns = [
    path('', inicio),
    path('paleta',paletas)
]