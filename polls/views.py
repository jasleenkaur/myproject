from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    question = Question.objects.all()
      
    template = loader.get_template('polls/index.html')
    context = {
        'question' : question,
    }
    return HttpResponse(template.render(context, request))
