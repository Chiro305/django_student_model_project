from django.http import HttpResponse

def home(r):
    return HttpResponse("<h1>Home Page</h1>")

def displayname(req, name):
    return HttpResponse("<h1>My name is=" + name + "</h1>")

def colourname(req, colours):
    colours={1:"red",2:"green", 3:"blue"}
    return HttpResponse(colours[1])
 