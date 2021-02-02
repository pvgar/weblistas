from django import forms
from django.http import HttpResponseRedirect 
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Nueva Tarea")
    # priority = forms.IntegerField(label="Prioridad", min_value=1, max_value=10)

# Create your views here.

def index(request):
    if "lista" not in request.session:
        request.session["lista"] = []

    return render(request, "listas/index.html", {
        "lista": request.session["lista"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["lista"] += [task]
            return HttpResponseRedirect(reverse("listas:index"))
        else:
           return render(request, "listas/add.html", {
                "form": form 
            })

    return render(request, "listas/add.html", {
        "form": NewTaskForm()
    })