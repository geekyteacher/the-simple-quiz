from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
# def index(request):
#     return HttpResponse("Testing...1..2..3")

def quizHome(request):
    template = loader.get_template('quiz/index.html')
    question_list = Question.objects.order_by('id')

    request.session['question_list'] = question_list

    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))

# def index(request):
#     latest_question_list = Question.objects.order_by('id')[:5]
#     output = ', '.join([q.questionText for q in latest_question_list])
#     return HttpResponse(output)

def showQuestion(request):
    question_list = request.session['question_list']
    template = loader.get_template('quiz/questions.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))