from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("This is personal portfolio home page")