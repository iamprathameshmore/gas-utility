
from django.urls import path, include
from . import views

app_name = 'manager'
urlpatterns = [
   
    path('', views.index),
]
