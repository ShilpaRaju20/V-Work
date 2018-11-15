from django.shortcuts import render, redirect
from . import forms
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import contractor_reg
from . import models
import socket

socket.getaddrinfo('localhost', 8080)


def contractor(request):
    model_object = contractor_reg.objects.all()

    if request.method == 'POST':
        form = forms.Contractor_forms(request.POST, request.FILES)
        if form.is_valid():
            # instance = form.save(commit=False)
            obj = form.cleaned_data
            contname = obj['contractor_name']
            gender = obj['gender']
            mail = obj['mail_id']
            phno = obj['phno']
            aadhar = obj['aadharno']
            add = obj['address']
            street = obj['street']
            city = obj['city']
            pin = obj['pin']
            district = obj['district']
            uname = obj['username']
            pwd = obj['pswd']
            con_categoryid = obj['con_categoryid']
            state_id = obj['state_id']
            cspwd = obj['confirm_pswd']
            minlen=8
            if contractor_reg.objects.filter(username=uname).exists():
                messages.info(request, 'username already exists')
            elif len(cspwd) < minlen:
                messages.info(request, 'Password should be atleast 8 characters')
            elif pwd == cspwd:
                a = contractor_reg(contractor_name=contname, gender=gender, mail_id=mail, phno=phno, aadharno=aadhar,
                                   address=add, street=street, city=city, pin=pin, district=district, username=uname,
                                   pswd=pwd, con_categoryid=con_categoryid, state_id=state_id)
                a.save()
                email = EmailMessage('VWork-Contractor Registration', 'You are successfully registered! username:    ' + uname + '       password:' + pwd + '',to=[mail])
                email.send()
                messages.info(request, 'Inserted Successfully')
                return redirect('contractor_reg:Contractor_forms')
            else:
                messages.info(request, 'Password mismatch')
                form = forms.Contractor_forms
        return render(request, "contractor/contractor.html", {'form': form})
    else:
        form = forms.Contractor_forms
        msg = "Not inserted"

    return render(request, "contractor/contractor.html", {'form': form, 'msg': msg, 'data': model_object})
