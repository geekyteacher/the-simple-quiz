from django.urls import include, path
from  . import views

urlpatterns = [
    path('', views.quizHome, name = 'quizHome'),
    path('quiz/', views.showQuestion, name = 'showQuestion'),
]