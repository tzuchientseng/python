# MVC架構: Model/View/Controller

from django.shortcuts import render

def second(request):
    return render(request, 'second.html')

def third(request):
    return render(request, 'third.html')

def index(request):
    context = {'name': 'Django'}
    return render(request, 'index.html', context) # **context 自動解包
# <h1>歡迎，{{ name }}！</h1>
