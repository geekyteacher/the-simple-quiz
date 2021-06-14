from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
# def index(request):
#     return HttpResponse("Testing...1..2..3")

def quizHome(request):
    return HttpResponse("QUIZ --- Testing...1..2..3")

# def index(request):
#     latest_question_list = Question.objects.order_by('id')[:5]
#     output = ', '.join([q.questionText for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    latest_question_list = Question.objects.order_by('id')[:5]
    template = loader.get_template('quiz/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))