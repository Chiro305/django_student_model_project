from django.shortcuts import render
from .models import Pets, Books

# Create your views here.


def index(req):
    allpets = Pets.objects.all()
    allbooks = Books.objects.all()
    # print(allpets)
    # print(allbooks)
    context = {"allpets": allpets, "allbooks": allbooks}
    return render(req, "index.html", context)

def allbooks(req):
    allpets = Pets.objects.all()
    context = {"allbooks": allbooks}
    return render(req, "index.html", context)

def allpets(req):
    allpets = Pets.objects.all()
    context = {"allpets": allpets}
    return render(req, "index.html", context)