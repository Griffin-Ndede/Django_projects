import datetime
from django.contrib import admin
from django.utils import timezone
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    #modifies the display on the admin dashboard
    @admin.display(
            boolean=True,
            ordering="publish_date",
            description="Published recently?"
    )
    # method that is used in the admin dashboard to check whether something has been published recently
    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__ (self):
        return self.choice_text