from django import forms
from . import models


class Contractor_forms(forms.ModelForm):
    confirm_pswd = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput())

    class Meta:
        model = models.contractor_reg
        fields = ['contractor_name', 'gender', 'mail_id', 'phno', 'aadharno', 'address', 'street', 'city', 'pin', 'district', 'username', 'pswd', 'con_categoryid', 'state_id', 'pin']

