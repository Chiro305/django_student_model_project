from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View


class ClassviewDemo(View):
    def get(self,request):
        return HttpResponse("<h1>Welcome to Django classview </h1>")
    
class HomeClassviews(ClassviewDemo):
    def get(self, r):
        return HttpResponse("<h1> Home Page</h1>")
    
def main(r):
    name="itvedant"
    return HttpResponse(f"<h1>This is main page</h1>{name}")