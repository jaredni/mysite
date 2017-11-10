from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from polls.forms.question_form import QuestionForm
from polls.models import Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all()


class CreateQuestion(generic.CreateView):
    model = Question
    template_name = 'polls/createquestion.html'
    form_class = QuestionForm

# Create your views here.
