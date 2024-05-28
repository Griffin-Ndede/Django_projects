from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question

# Create your views here.
def home(request):
    question_list = Question.objects.order_by("publish_date")
    context = {"question_list": question_list}
    return render(request, "questions.html", context)

def detail(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, "details.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)