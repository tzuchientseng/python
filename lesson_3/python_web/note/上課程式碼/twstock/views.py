from django.shortcuts import render
from G import G
# Create your views here.
def html(request):
    info = G.saveHistory(request, 'twstock')
    request.session["currentPage"] = "/twstock"
    return render(request, "twstock.html",{'info':info[1],"userAccount":G.userAccount(request)})