from django import forms
from . import models


class Employee_Forms(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ['emp_name', 'gender', 'mail_id', 'phno', 'aadharno', 'address', 'street', 'city', 'pin', 'district', 'state_id', 'contractorcat_id']