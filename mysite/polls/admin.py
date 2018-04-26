from django.contrib import admin
from .models import Question, Choice, QuestionAdmin

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
