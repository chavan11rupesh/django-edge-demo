from django.contrib import admin
from .models import Question, Choice
from rangefilter.filter import DateRangeFilter
from django.utils.html import format_html


class QuestionAdmin(admin.ModelAdmin):
    # to not show selected counter
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/my_app/my_model/{}/delete/">Delete</a>', obj.id)
    actions_selection_counter = False
    # to show dates
    date_hierarchy = 'date_created'
    # to add search bar
    search_fields = ['set_no','level_no']
    # to show only required fields on admin panel
    list_display = ('practice_question','answer','set_no','level_no','delete_button')
    # to add filter on the right side
    list_filter = ('practice_question','set_no',('date_created',DateRangeFilter))
    # to add sections while adding data
    fieldsets = (
        ('Section1',{
            'fields' : ('practice_question','answer')
        }),
        ('Section2',{
            'fields' : ('hint1','hint2','hint3')
        }),
        ('Section3',{
            'fields' : (('set_no','level_no'),'date_created')
        }),)
    # to show empty value
    empty_value_display = '-empty-'


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
