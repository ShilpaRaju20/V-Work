from django import forms
from . import models


class ConCategory_Forms(forms.ModelForm):
    class Meta:
        model = models.ContractorCategory
        fields = ['concategoryname', 'concategorydesc']
