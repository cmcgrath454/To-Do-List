from re import L
from socket import fromshare
from typing import List
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import List, Task
from django import forms

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def view_all_lists(request):
    lists = List.objects.all()
    return render(request, 'index.html', {'lists':lists})

def view_list(request, id):
    list = List.objects.get(id=id)
    tasks = Task.objects.filter(list=list)
    return render(request, 'list.html', {'list':list, 'tasks':tasks})

class list_form(forms.form):
    name = forms.CharField(label="name", max_length=25)

def new_list(request):
    if request.method == 'POST':
        form = list_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('index.html')
    else:
        form = list_form()

    return render(request, 'list_form.html', {'form' : form})
