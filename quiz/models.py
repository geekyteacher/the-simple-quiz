from django.db import models

# Create your models here.
class Question(models.Model):
    questionText = models.CharField(max_length = 240)
    correctAnswer = models.CharField(max_length = 140, default='')
    incorrectAnswer1 = models.CharField(max_length = 140, default='')
    incorrectAnswer2 = models.CharField(max_length = 140, blank = True, default='')
    incorrectAnswer3 = models.CharField(max_length = 140, blank = True, default='')

    def __str__(self):
        return self.questionText
        
    class Meta:
        verbose_name = 'Questions'
        verbose_name_plural = 'Questions'