from django.shortcuts import render
from datetime import datetime
# Create your views here.


def index(req):
    dt = datetime.now()
    hour = dt.hour
    if 4 <= hour < 12:
        greeting = "Good Morning 🌞"
    elif 12 <= hour < 16:
        greeting = "Good Afternoon 🌤️🌇"
    elif 16 <= hour < 20:
        greeting = "Good Evening 🌆"
    else:
        greeting = "Good Night 🌉"
    print(greeting)
    context = {"greeting": greeting}
    return render(req, "index.html", context)



def loginuser(req):
    return render(req, "loginuser.html")


def registeruser(req):
    return render(req, "registeruser.html")


def aboutus(req):
    return render(req, "aboutus.html")


def contactus(req):
    return render(req, "contactus.html")

