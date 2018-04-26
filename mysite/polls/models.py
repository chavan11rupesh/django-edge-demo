import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.admin import DateFieldListFilter


class CSSAdminMixin(object):
    class Media:
        css = {
            'all' : ('css/admin.css',),
        }


class Question(models.Model):
    practice_question = models.TextField()
    answer = models.TextField()
    hint1 = models.TextField()
    hint2 = models.TextField()
    hint3 = models.TextField()
    set_no = models.IntegerField(default=0)
    level_no = models.IntegerField(default=0)
    date_created = models.DateTimeField()


class QuestionAdmin(admin.ModelAdmin):
    #to add search bar
    search_fields = ['set_no','level_no']
    # to show only required fields on admin panel
    list_display = ('practice_question','answer','set_no','level_no')
    # to add filter on the right side
    list_filter = ('practice_question','set_no',('date_created',DateFieldListFilter))
    # to add sections while adding data
    fieldsets = (
        ('Section1',{
            'fields' : ('practice_question','answer')
        }),
        ('Section2',{
            'fields' : ('hint1','hint2','hint3')
        }),
        ('Section3',{
            'fields' : ('set_no','level_no','date_created')
        })
    )



class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
