from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('newsbase', views.newsbase, name='General News'),
    path('sports', views.sports, name='Sports News'),
    path('business', views.business, name= 'Business News'),

]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='home'),
#     path('news_base', views.news_base, name='base'),
#     path('sports', views.sports, name='sports'),
#     path('business', views.business, name='business'),
# ]