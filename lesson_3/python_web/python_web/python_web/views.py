"""
這個是自訂義的檔案
"""
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')
