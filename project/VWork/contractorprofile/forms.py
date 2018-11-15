from django import forms
from contractor_reg.models import contractor_reg


class Profile_Forms(forms.ModelForm):

    class Meta:
        model = contractor_reg
        fields = ['contractor_name', 'gender', 'mail_id', 'phno', 'aadharno', 'address', 'street', 'city', 'pin', 'district', 'username', 'pswd', 'con_categoryid', 'state_id', 'pin']

