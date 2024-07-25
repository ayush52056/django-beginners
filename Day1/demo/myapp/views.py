from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "myapp/home.html")


def todos(request):
    items = TodoItem.objects.all()
    return render(request,"myapp/todo.html",{"todos": items})