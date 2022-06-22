import random
from django.shortcuts import render

def about (request):
    return render(request, 'generator/about.html')

def home (request):
    return render(request, 'generator/home.html')

def password(request):

    caracteres = list('abcdefghijklmnñopqrstuvwxyz')
    generador_contraseña = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        caracteres.extend(list('!@#$%&*-_.,+'))
    if request.GET.get('numbers'):
        caracteres.extend(list('123456789'))
    


    for c in range(length):
        generador_contraseña += random.choice(caracteres)

    return render(request, 'generator/password.html', {'password':generador_contraseña})