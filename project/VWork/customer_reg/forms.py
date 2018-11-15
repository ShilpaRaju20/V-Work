from django import forms
from . import models


class Customer_Forms(forms.ModelForm):

    class Meta:
        model = models.Customer_Reg
        fields = ['cust_name', 'gender', 'cust_mailid',  'cust_phno', 'cust_aadharno', 'cust_address', 'cust_street', 'cust_city', 'cust_pin', 'cust_district', 'cust_uname', 'cust_pswd', 'state_id']