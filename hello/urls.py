from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #when we have a url which is a string, call the greet function
    path("<str:name>", views.greet, name="greet"), 
    path("ghazal", views.ghazal, name="ghazal")
]