"""
URL configuration for Bird_Academy project.

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
from django.urls import path, include
from Application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('addBird/', views.addBird, name="addBird"),
    path('quizz/', views.quizz, name="quizz"),
    path('accounts/', include('accounts.urls')),
    path('api/user_birds/', views.get_user_birds, name='get_user_birds'),
    path('api/user_songs/', views.get_song_birds_user, name='get_song_birds_user'),
]
