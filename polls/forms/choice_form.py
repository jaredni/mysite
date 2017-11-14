from django import forms

from polls.models import Choice


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        exclude = ('question', 'votes')
