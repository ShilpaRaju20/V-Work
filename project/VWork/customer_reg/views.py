from django.shortcuts import render, redirect
from . import forms
from django.core.mail import EmailMessage
# from .models import Customer_Reg


def customer(request):
    if request.method == 'POST':
        form = forms.Customer_Forms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            obj = form.cleaned_data
            mail = obj['cust_mailid']
            uname = obj['cust_uname']
            pswd = obj['cust_pswd']
            instance.save()
            msg = "Successfully Inserted"
            email = EmailMessage('VWork-Customer Registration!', 'You are successfully registered! username:    ' + uname + '       password:' + pswd + '', to=[mail])
            email.send()
            return redirect('customer_reg:Customer_Forms')
    else:
        form = forms.Customer_Forms
        msg = "Unsuccessful"

    return render(request, "customerregistration/customerreg.html", {'form': form, 'msg': msg})
    # return render(request, "customerregistration/customerreg.html", {'form': form, 'msg': msg})
