"""quick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from coronacases import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('^$',views.index,name='Main page'),
    # url('index', views.index, name='Main page'),
    path('', include('home.urls')),
    path('signupapp/', include('signupapp.urls')),
    path('loginapp/', include('loginapp.urls')),
    path('news/', include('news.urls')),
    path('logout/', include('logout.urls')),
    path('coronacases/', include('coronacases.urls')),


]
