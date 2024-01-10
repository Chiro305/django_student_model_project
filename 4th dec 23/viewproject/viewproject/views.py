from django.http import HttpResponse
from django.shortcuts import redirect


def home(r):
    return HttpResponse("<h1>Welcome to Django world<br><a href='login'>Login</a></h1>")

def login(r):
    return redirect("/index")


def index(r):
    print("Calculator App")
    a = int(input("Enter a ="))
    b = int(input("Enter b ="))
    print("a =",a)
    print("b =",b)
    output = f"<h1>Calculator App1<br>a={a}<br>b={b}<br>Addition={a+b}</h1>"
    # return HttpResponse("a ="+ str(a) + " " + "b=" + str(b) + " " + "addition=" + str(a + b))
    return HttpResponse(output + "<br><h1><a href='/'>Home</a></h1>")
