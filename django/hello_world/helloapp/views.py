from django.shortcuts import render
from django.http import HttpResponse

def helloworldview(request):
    return HttpResponse("hello app load")
# Create your views here.
