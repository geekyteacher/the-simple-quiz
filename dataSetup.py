from quiz.models import Question
from django.utils import timezone

q = Question(
    questionText = "What is the connection between Windows, macOS, Ubuntu and Android?", 
    correctAnswer = "Operating systems",
    incorrectAnswer1 = "Chocolate bars",
    incorrectAnswer2 = "Software",
    incorrectAnswer3 = "Computer systems")

q.save()

#Find more efficeint way
#Questionsin text file, import loop