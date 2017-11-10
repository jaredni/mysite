from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^createquestion/$',
        views.CreateQuestion.as_view(), name='createquestion'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/result/$',
        views.ResultView.as_view(), name='result'),
]
