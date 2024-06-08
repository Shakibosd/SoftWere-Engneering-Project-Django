from django.shortcuts import render, redirect
from . models import TaskModel
from . forms import TaskForm


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_tasks")
    else:
        form = TaskForm()
    return render(request, "./task/add_task.html", {'form' : form})        

def edit_task(request, id):
    task = TaskModel.objects.get(id=id)
    task_form = TaskForm(instance=task)   
    if request.method == 'POST':    
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')

    return render(request, './task/edit_task.html', {'form': task_form})    


def delete_task(request, id):
    task = TaskModel.objects.get(id=id)
    task.delete()
    return redirect('show_tasks')

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request,'./task/show_tasks.html', {'tasks' : tasks})