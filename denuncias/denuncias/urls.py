from django.urls import path
from vigilante.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('denuncias', denuncias, name='denuncias'),
    path('contacto', contacto, name='contacto'),
    path('about', sobre, name='sobre'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('dashboard', dashboard, name='dashboard'),
    path('misdenuncias', misdenuncias, name='misdenuncias'),
]
