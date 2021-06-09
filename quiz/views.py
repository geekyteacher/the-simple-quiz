from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Testing...1..2..3")

def quizHome(request):
    return HttpResponse("QUIZ --- Testing...1..2..3")