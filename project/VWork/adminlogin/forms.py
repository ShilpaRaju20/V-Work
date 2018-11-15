from django import forms



class AdminLogin_Forms(forms.Form):
    username = forms.CharField(required=True, label='Username', max_length=30)
    password = forms.CharField(required=True, label='Password', max_length=30, widget=forms.PasswordInput())

