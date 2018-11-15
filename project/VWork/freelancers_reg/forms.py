from django import forms
from . import models


class Freelancer_Forms(forms.ModelForm):

    class Meta:
        model = models.Freelancers_Reg
        fields = ['name', 'gender', 'mail_id', 'phno', 'aadhar_no', 'address', 'street', 'city', 'pin', 'district', 'work_categoryid']

