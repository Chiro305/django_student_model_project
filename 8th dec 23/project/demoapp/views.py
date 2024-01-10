from django.shortcuts import render, HttpResponse


def index(r):
    print("App started")
    return HttpResponse("Welcome to my webpage")