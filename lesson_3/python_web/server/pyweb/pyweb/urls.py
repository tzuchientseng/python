"""
URL configuration for pyweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# import first, views
import home.views as home
import gallery.views as gallery
from session import views as session

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('first', first.html),
    path('second/', views.second),
    path('third/', views.third),
    # path('third/', views.index),
    path('', home.html), # html 不是副檔名是方法
    path('gallery/', gallery.html),
    path("login/", session.login),
    path("logout/", session.logout),
    path("login_process/", session.login_process),
    path("check_session/", session.check_session),
    path("reject/", session.reject),
]
