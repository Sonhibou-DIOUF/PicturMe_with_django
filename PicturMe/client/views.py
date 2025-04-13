from django.shortcuts import render
from django.http import HttpResponse

def hello_client(request):
    return HttpResponse('<h1>Hello HttpResponse</h1>')    