from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

def index(request):
    p = Post.objects.all()
    template = loader.get_template('blog/index.html')
    context = {
        'posts': p,
    }
    
    return HttpResponse(template.render(context, request))

