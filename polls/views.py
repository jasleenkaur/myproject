from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,Http404
from .models import Question, Choice

def index(request):
    question = Question.objects.all()
      
    template = loader.get_template('polls/index.html')
    context = {
        'question' : question,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question with id = %s does not exixt" %question_id)
    return HttpResponse("this is details page: %s" %question_id)

def vote(request, question_id):
    return HttpResponse("this is vote page: %s" %question_id)

def results(request, question_id):
    return HttpResponse("this is result page: %s" %question_id)
