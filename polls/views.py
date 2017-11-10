from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from polls.models import Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all()

# Create your views here.
