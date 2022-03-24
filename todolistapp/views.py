from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def view_all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks':tasks})

def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            return redirect('')
    else:
        form = TaskForm()
    return render(request, 'new_task.html', {'form' : form})

def update_task(request, id):
    instance = get_object_or_404(Task, id=id)
    form = TaskForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('')
    return render(request, 'update_task.html', {'form': form})

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('')

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name']
