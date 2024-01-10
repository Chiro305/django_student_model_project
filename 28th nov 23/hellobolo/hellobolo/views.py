from django.http import HttpResponse

def index(request):
    print("Thank You Server")
    return HttpResponse("<h1>Welcome To DDDDDDJango World!!!!</h1>")

def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def register(request):
    return HttpResponse("<h1>Register Page</h1>")

def login(request):
    return HttpResponse("<h1>Login Page</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Page</h1>")