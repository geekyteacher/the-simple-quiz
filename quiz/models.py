from django.db import models

# Create your models here.
class Question(models.Model):
    questionText = models.CharField(max_length = 240)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choiceText = models.CharField(max_length = 140)
    correct = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'Questions'
        verbose_name_plural = 'Questions'