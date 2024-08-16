from django.shortcuts import render
from django import forms

tasks= ["foo", "bar", "baz"]

class NewTaskFrom(forms.Form):
    task= forms.CharField(label= "new task")
    priority = forms.IntegerField(label ="priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        form= NewTaskFrom(request.POST)
        if form.is_valid(): #if the form is valid 
            task=form.cleaned_data["task"]   #get the data from the form, get the "task" and save in task variable
            tasks.append(task)
        else:
            return render(request, "tasks/add.html", { #return the file again and display the existing form
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form" : NewTaskFrom()
    })