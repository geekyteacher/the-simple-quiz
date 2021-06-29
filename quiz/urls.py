from django.urls import include, path
from  . import views

urlpatterns = [
    path('', views.showQuestion, name = 'showQuestion'),
    path('quiz/', views.quizHome, name = 'quizHome'),
]