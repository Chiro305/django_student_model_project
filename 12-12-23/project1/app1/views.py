from django.shortcuts import render,HttpResponse

# Create your views here.
def showapp(r):
    return HttpResponse("Welcome app1")