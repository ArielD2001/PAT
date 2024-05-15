import requests
from django.shortcuts import render


def inicio(request):
    # Realizar una solicitud a la API de noticias
    url = 'https://newsapi.org/v2/everything?'
    params = {
        'apiKey': '5b4cff4ceb1d4b028dbd924b74ef2d4e',
        'q': ' denuncias en cartagena',  # Ejemplo: buscar noticias relacionadas con Cartagena
        'from': '2024-05-14&',
        'language': 'es',  # Establecer el idioma de las noticias
        'sortBy': 'popularity',  # Ordenar por fecha de publicación
        'pageSize':'5',
        'page':'1',

    }
    response = requests.get(url, params=params)

    # Procesar la respuesta de la API
    if response.status_code == 200:
        noticias = response.json()['articles']

        
    else:
        noticias = None

    # Renderizar los datos en la plantilla
    return render(request, 'inicio.html', {'noticias': noticias})


def denuncias(request):
    return render(request, 'denuncias.html')

def contacto(request):
    return render(request, 'contacto.html')

def sobre(request):
    return render(request, 'sobre.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def misdenuncias(request):
    return render(request, 'misdenuncias.html')


