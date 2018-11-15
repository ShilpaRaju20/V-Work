from django import forms
from contractor_reg.models import contractor_reg


class Login_Forms(forms.Form):
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
        model = contractor_reg
        fields = ['name']