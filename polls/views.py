from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse,Http404
from .models import Question, Choice

def index(request):
    question_list = Question.objects.all()
      
    template = loader.get_template('polls/index.html')
    context = {
        'question_list' : question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/details.html', {'question' : question,})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    choice = question.choice_set.get(pk=request.POST['choice'])
    return render(request, 'polls/vote.html', {'question' : question, 'choice' : choice})

def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return HttpResponse("this is result page: %s" %question_id)
