from django.urls import path
from . import views


urlpatterns =[
    path("",views.showapp3,name="showapp3")
]