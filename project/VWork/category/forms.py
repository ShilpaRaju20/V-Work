from django import forms
from . import models


class Category_Forms(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['categoryname']
