from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import List, Task
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def view_all_lists(request):
    lists = List.objects.all()
    return render(request, 'index.html', {'lists':lists})

def view_list(request, id):
    list = List.objects.get(id=id)
    tasks = Task.objects.filter(list=list)
    return render(request, 'list.html', {'list':list, 'tasks':tasks})

def new_list(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            created_list = form.save()
            return HttpResponseRedirect('')
    else:
        form = ListForm()

    return render(request, 'new_list.html', {'form' : form})

def update_list(request, id):
    instance = get_object_or_404(List, id=id)
    form = ListForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('')
    return render(request, 'update_list.html', {'form': form})

def delete_list(request, id):
    list = List.objects.get(id=id)
    if request.method == 'POST':
        list.delete()
    return redirect('')

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ['name']

