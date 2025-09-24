from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello FBAS_Nov_23_2_ru from product app")
