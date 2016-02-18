from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo
def index(request):
    todos = Todo.objects.all()
    not_done = Todo.objects.filter(status=False)
    done = Todo.objects.filter(status=True)
    template = loader.get_template("todo/index.html")
    context = {
    'todos' : todos,
    'not_done' : not_done,
    'done' : done,
    }
    return HttpResponse(template.render(context, request))
