from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.showapp2,name="showapp2"),
]