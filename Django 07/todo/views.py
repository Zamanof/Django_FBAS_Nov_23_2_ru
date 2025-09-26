from django.shortcuts import render
from django.http import HttpResponse
from . import models
def index(request):
    # return HttpResponse("todo")
    tasks = models.Task.objects.all()
    # return HttpResponse([str(task) +'<br/>' for task in tasks])
    return render(request, 'tasks.html', {'tasks':tasks})

