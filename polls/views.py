from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.http import (
    HttpResponseRedirect, HttpResponse, Http404)
from django.core.urlresolvers import reverse, reverse_lazy

from polls.forms.question_form import QuestionForm
from polls.forms.choice_form import ChoiceForm
from polls.models import Question, Choice

from django.conf import settings

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all()


class CreateQuestion(generic.CreateView):
    model = Question
    template_name = 'polls/createquestion.html'
    form_class = QuestionForm
    success_url = reverse_lazy('polls:index')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

    def post(self, request, *args, **kwargs):
        q = Question.objects.get(pk=self.request.POST['question'])
        print q.id
        try:
            choice = Choice.objects.get(pk=self.request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            print 'no choice selected'
            return HttpResponseRedirect(reverse('polls:detail', args=(q.id,)))
        else:
            choice.votes += settings.VOTE_VALUE
            choice.save()
            return super(ResultView, self).get(request, *args, **kwargs)

# Create your views here.
