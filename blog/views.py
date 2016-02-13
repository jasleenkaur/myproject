from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
from .forms import PostForm

def index(request):
    p = Post.objects.all()
    template = loader.get_template('blog/index.html')
    context = {
        'posts': p,
    }
    
    return HttpResponse(template.render(context, request))

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
