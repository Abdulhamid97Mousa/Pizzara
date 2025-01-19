from django.shortcuts import render, redirect

from project.models import Project

from .models import TodoList
from django.contrib.auth.decorators import login_required


@login_required
def todolist(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = TodoList.objects.filter(project=project_id).get(pk=pk)
    
    
    
    return render(request, 'todolist/todolist.html', {
        'project': project,
        'todolist': todolist
    })
    

@login_required
def add(request, project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        
        if name:
            TodoList.objects.create(
                name=name, description=description,
                project=project, created_by=request.user
            )
            return redirect(f'/projects/{project_id}/')
        else:
            print("Not valid")
    
    return render(request, 'todolist/add.html', {
    'project': project
    })




@login_required
def edit(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = TodoList.objects.filter(project=project_id).get(pk=pk)
    
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        
        if name:
            todolist.name = name
            todolist.description = description
            todolist.save()
            return redirect(f'/projects/{project_id}/{pk}/')
        else:
            print("Not valid")
    
    return render(request, 'todolist/edit.html', {
        'project': project,
        'todolist': todolist
    })
    
    
@login_required
def delete(request, project_id, pk):
    Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = TodoList.objects.filter(project=project_id).get(pk=pk)
    todolist.delete()
    return redirect(f'/projects/{project_id}/')

@login_required
def back(request, project_id, pk):
    Project.objects.filter(created_by=request.user).get(pk=project_id)
    TodoList.objects.filter(project=project_id).get(pk=pk)
    
    return redirect(f'/projects/{project_id}/')