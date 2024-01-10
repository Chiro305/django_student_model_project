from django.shortcuts import render

# Create your views here.


def index(req):
    return render(req, "index.html")


def loginuser(req):
    return render(req, "loginuser.html")


def registeruser(req):
    return render(req, "registeruser.html")


def aboutus(req):
    return render(req, "aboutus.html")


def contactus(req):
    return render(req, "contactus.html")
