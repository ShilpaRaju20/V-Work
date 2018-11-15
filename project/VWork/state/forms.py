from django import forms
from . import models


class State_Forms(forms.ModelForm):
    class Meta:
        model = models.State
        fields = ['name']
