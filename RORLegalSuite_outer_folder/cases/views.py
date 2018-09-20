#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def cases(request):
    return HttpResponse("Master List of Cases")