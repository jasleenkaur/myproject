from django.contrib import admin
from .models import Question, Choice

#StackedInline will create all choice inline to question but in stacked manner. 
#Here tabular in line is used which will create more compact representation.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text','pub_date']
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_date','was_published_recently']
    search_fields = ['question_text']
    list_filter = ['question_text','pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
#admin.site.site_header = "My Project"
