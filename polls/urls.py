from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^createquestion/$',
        views.CreateQuestion.as_view(), name='createquestion'),
]
