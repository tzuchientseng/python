from django.shortcuts import render, redirect

# Create your views here.

def html(request):
    request.session["currentPage"] = "/gallery"
    if 'userAcount' not in request.session:
        return  redirect('/login')
    return render(request, 'gallery.html')
