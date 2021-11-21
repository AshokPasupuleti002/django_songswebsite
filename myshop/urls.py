"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from songs.views import index, aboutus, Movies, home, movie_details, audio, video, search_list, contactus, thankyou, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index', home),
    path('aboutus', aboutus),
    path('movies', Movies),
    path('movie_details<int:x>', movie_details),
    path('audio', audio),
    path('video', video),
    path('search_list', search_list),
    path('contactus', contactus),
    path('thankyou', thankyou),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
