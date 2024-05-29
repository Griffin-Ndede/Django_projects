from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F


from .models import Question, Choice

# Create your views here.
def home(request):
    question_list = Question.objects.order_by("publish_date")
    context = {"question_list": question_list}
    return render(request, "questions.html", context)

def detail(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, "details.html", {"question": question})

def results(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, "results.html", {"question": question})

def vote(request, id):
    question = get_object_or_404(Question, pk=id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))