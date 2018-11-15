from django import forms
from . import models


class Work_Forms(forms.ModelForm):
    class Meta:
        model = models.Works
        fields = ['work_name', 'constructioncat_id', 'work_date', 'amt', 'images']