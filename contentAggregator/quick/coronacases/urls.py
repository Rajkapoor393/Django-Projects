from django.contrib import admin
from django.urls import path
# from firstPage import views
from django.conf.urls import url
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    url('index',views.index,name='Main page'),
    url('index', views.index, name='CoronaCases'),
]