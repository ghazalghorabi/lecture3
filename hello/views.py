from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def ghazal(request):
    return HttpResponse("hello ghazal")

def greet(request,name):    #take the string (name) as an argument
    return render(request, "hello/greet.html", { #and render the html file
        "name": name.capitalize()   #and pass in the name 
    })