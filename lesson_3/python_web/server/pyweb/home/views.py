from django.shortcuts import render

# Create your views here.

def html(request):
    request.session["currentPage"] = "/"
    return render(request, 'home.html')
