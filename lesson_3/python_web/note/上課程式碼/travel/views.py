from django.shortcuts import render, redirect

from G import G
# Create your views here.
def html(request):
    info=G.saveHistory(request,'travel')
    request.session["currentPage"] = "/travel"
    if 'userAccount' not in request.session:
        return redirect("/login")
    return render(request, "travel.html",{'info':info[1],"userAccount":G.userAccount(request)})