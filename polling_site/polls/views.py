from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question

# Create your views here.
def home(request):
    question_list = Question.objects.order_by("publish_date")[:5]
    template = loader.get_template("questions.html")
    context = {
        "question_list": question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)