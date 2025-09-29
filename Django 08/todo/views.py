from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . import models


def index(request):
    # return HttpResponse("todo")
    tasks = models.Task.objects.all()
    # return HttpResponse([str(task) +'<br/>' for task in tasks])
    return render(request, 'tasks.html', {'tasks':tasks})

def detail(request, task_id):
    # variant 1
    # try:
    #     task = models.Task.objects.get(pk=task_id)
    #     return render(request, 'detail.html', {'task':task})
    # except models.Task.DoesNotExist:
    #     raise Http404
    # variant 2
    task = get_object_or_404(models.Task, pk=task_id)
    return render(request, 'detail.html', {'task':task})

