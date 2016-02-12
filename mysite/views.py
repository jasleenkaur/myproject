from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question
from blog.models import Post

def index(request):
    q = Question.objects.all()
    p = Post.objects.all()
    context = {
    'question' : q,
    'post' : p,
    }
    return render(request, 'index.html', context)
    
