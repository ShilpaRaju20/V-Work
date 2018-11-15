from django import forms
from .import models


class Complaint_Forms(forms.ModelForm):
    complaint = forms.CharField(required=True, label='complaint', max_length=30, widget=forms.TextInput(attrs={'pattern': '[A-Za-z]+', 'title': 'enter numeric character only'}))

    class Meta:
        model = models.Complaint
        fields = ['contractor_name', 'cdate', 'complaint']
