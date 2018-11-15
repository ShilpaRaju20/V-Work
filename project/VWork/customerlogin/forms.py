from django import forms
from customer_reg.models import Customer_Reg


class Custlogin_Forms(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32

    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = Customer_Reg
        fields = ['name']
