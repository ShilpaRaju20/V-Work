from django import forms
from . import models


class Approach_Forms(forms.ModelForm):
    class Meta:
        model = models.Approach
        fields = ['amt', 'cdate']


