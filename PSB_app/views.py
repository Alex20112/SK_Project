from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Root(request):
    return HttpResponse('Привет')