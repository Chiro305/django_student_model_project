from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import RegisterStudent
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def allstudents(r):
    if r.user.is_authenticated:
        username = r.user
        studentdata = Student.objects.all()
        context = {"studentdata": studentdata,"username": username}
        return render(r,"allstudents.html", context)
    else:
         studentdata = Student.objects.all()
         context = {"studentdata": studentdata}
         return render(r,"allstudents.html", context)

def studentdetails(r,studentid):
    studentrecord = Student.objects.get(studentid=studentid)
    context = {"studentrecord": studentrecord}
    return render(r, "studentdetails.html",context)
def deletestudents(r,studentid):
     studentrecord = Student.objects.get(studentid=studentid)
     studentrecord.delete()
     return redirect("/")

def registerstudent(r):
    if r.method == "GET":
        context = {}
        form = RegisterStudent()
        context["form"] = form
        return render(r,"registerstudent.html",context)

    else:
        context ={}
        form = RegisterStudent(r.POST or None)
        if form.is_valid():
            form.save()
        context["form"] = form
        return redirect("/")
    

def updatestudent(req, studentid):
    # studentrecord = get_object_or_404(Student, studentid=studentid)
    studentrecord = Student.objects.get(studentid=studentid)
    if req.method == "POST":
        form = RegisterStudent(req.POST, req.FILES, instance=studentrecord)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterStudent(instance=studentrecord)

    context = {"form": form, "studentrecord": studentrecord}
    return render(req, "updatestudent.html", context)


def signup(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        ucpass = req.POST["ucpass"]
        context = {}
        if uname == "" or upass == "" or ucpass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signup.html", context)
        elif upass!=ucpass:
            context["errmsg"] = "Password and Confirm Password Dosen't match"
            return render(req, "signup.html", context)
        else:
            try:
                userdata = User.objects.create(username=uname, password=upass)
                userdata.set_password(upass)
                userdata.save()
                return redirect("/")
            except Exception as e:
                context["errmsg"] = "User Already Exist"
                return render(req, "signup.html", context)
    else:
        return render(req, "signup.html")

def signin(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        context = {}
        if uname == "" or upass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signup.html", context)
        else:
            userdata=authenticate(username=uname,password=upass)
            if userdata is not None:
                login(req,userdata)
                return redirect("/")
            else:
                context["errmsg"] = "Invalide username and Password"
                return render(req, "signin.html",context) 
    else:
        return render(req, "signin.html")
