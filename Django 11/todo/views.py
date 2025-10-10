from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages

from . import models
from .forms import TaskForm


def index(request):
    # return HttpResponse("todo")
    # return HttpResponse([str(task) +'<br/>' for task in tasks])
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, "Task added successfully")
            return redirect('todo:index')
    else:
        form = TaskForm()

    tasks = models.Task.objects.order_by("-id")
    return render(request, 'tasks.html', {'tasks':tasks, 'form':form})


def detail(request, task_id):
    # variant 1
    # try:
    #     task = models.Task.objects.get(pk=task_id)
    #     return render(request, 'detail.html', {'task':task})
    # except models.Task.DoesNotExist:
    #     raise Http404
    # variant 2
    task = get_object_or_404(models.Task, pk=task_id, owner=request.user)
    return render(request, 'detail.html', {'task':task})


def toggle_done(request, task_id):
    task = get_object_or_404(models.Task, pk=task_id, owner=request.user)
    task.is_done = request.POST.get('is_done') == '1'
    task.save()
    return redirect("todo:index")