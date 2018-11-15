from django import forms
from . import models


class UserWork_Forms(forms.ModelForm):
    class Meta:
        model = models.UserWorks
        fields = ['userwork_date', 'work_plot', 'work_categoryname']
