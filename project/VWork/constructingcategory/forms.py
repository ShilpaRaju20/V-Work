from django import forms
from . import models


class ConstructCategory_Forms(forms.ModelForm):
    class Meta:
        model = models.ConstructingCategory
        fields = ['construction_name']
