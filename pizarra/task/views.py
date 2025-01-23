from django.shortcuts import render, redirect
from project.models import Project
from todolist.models import TodoList
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def task(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = TodoList.objects.filter(project=project).get(pk=todolist_id)
    task = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)
    
        
    if 'toggle_done' in request.GET:
        task.is_done = not task.is_done
        task.save()
    
    return render(request, 'task/task.html', {
        'task': task  
    })
    
@login_required
def add(request, project_id, todolist_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = TodoList.objects.filter(project=project_id).get(pk=todolist_id)
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        
        
        task = Task.objects.create(
                name=name, description=description,
                todolist=todolist, project=project, created_by=request.user
            )
        print("Task created", task)
        print("Task created", task.project)
        print("Task created", task.todolist)
        print("Task created", task.created_by)
        return redirect(f'/projects/{project_id}/{todolist_id}/')
    
    return render(request, 'task/add.html')


@login_required
def delete(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = TodoList.objects.filter(project=project_id).get(pk=todolist_id)
    task = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)
    task.delete()
    return redirect(f'/projects/{project_id}/{todolist_id}/')


@login_required
def edit(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = TodoList.objects.filter(project=project_id).get(pk=todolist_id)
    task = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        
        if name:
            task.name = name
            
        task.description = description
        task.save()
        return redirect(f'/projects/{project_id}/{todolist_id}/{pk}/')

    return render(request, 'task/edit.html', {
        'task': task
    })


@login_required
def back(request, project_id, todolist_id, pk):
    return redirect(f'/projects/{project_id}/{todolist_id}/')