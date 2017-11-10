from django import forms

from polls.models import Choice


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = '__all__'
