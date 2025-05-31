from django.shortcuts import render
from G import G
# Create your views here.
def html(request):
    info=G.saveHistory(request, 'twgold')
    request.session["currentPage"] = "/twgold"
    return render(request, "twgold.html",{'info':info[1],"userAccount":G.userAccount(request)})