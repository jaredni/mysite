from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.http import (
    HttpResponseRedirect, HttpResponse, Http404)
from django.core.urlresolvers import reverse

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

    def get_success_url(self):
            return reverse('polls:index')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# Create your views here.
