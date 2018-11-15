from django import forms
from . import models


class Feedback_Forms(forms.ModelForm):
    feedback = forms.CharField(required=True, label='feedback', max_length=30, widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'enter numeric character only'}))

    class Meta:
        model = models.Feedback
        fields = ['con_name', 'work_categoryname', 'fdate', 'feedback']

