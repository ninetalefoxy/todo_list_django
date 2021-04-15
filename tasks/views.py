from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):

    tasks = Task.objects.all()
    forms = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'tasks/list.html', {'tasks':tasks, 'forms':forms})

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'tasks/update_task.html',{'form':form})

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'tasks/delete.html',{'item':item})