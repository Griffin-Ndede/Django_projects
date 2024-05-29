from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# adds choices to the questions
# tabularinline - makes the choices align in a table
# stackedinline - aligns the choices in a column
class ChoiceInline(admin.TabularInline):
        model =Choice
        extra = 3

class QuestionAdmin(admin.ModelAdmin):
        # separates the different items into fields
        fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["publish_date"]}),
    ]
        list_display = ["question_text", "publish_date", "was_published_recently"]
        inlines = [ChoiceInline]
       
        # adds a sidebar filter by attribute given
        list_filter = ['publish_date']
        
        # adds search capability to the questions
        search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
