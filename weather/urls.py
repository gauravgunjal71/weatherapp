from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('getweather', views.getweather)
]