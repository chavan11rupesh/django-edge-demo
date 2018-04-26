import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    practice_question = models.TextField()
    answer = models.TextField()
    hint1 = models.TextField()
    hint2 = models.TextField()
    hint3 = models.TextField()
    set_no = models.IntegerField(default=0)
    level_no = models.IntegerField(default=0)
    date_created = models.DateTimeField()


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
