import gc

from django.shortcuts import render, redirect
from G import G
# Create your views here.
def html(request):
    info=G.saveHistory(request,'tools')
    request.session["currentPage"] = "/tools"
    if 'userAccount' not in request.session:
        return redirect("/login")
    print("成功了===================")
    return render(request, "tools.html",{'info':info[1],"userAccount":G.userAccount(request)})