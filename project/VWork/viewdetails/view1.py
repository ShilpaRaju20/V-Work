from django.shortcuts import render
from django.db import connection
from approach.models import Approach
from django.core.mail import EmailMessage


def view1(request, pk):

    login_id = request.session['logid']
    modelobject = Approach.objects.get(id=pk)
    modelobject1 = Approach.objects.filter(id=pk)
    mail = modelobject1.mail_id
    email = EmailMessage('you are selected',  to=[mail])
    email.send()
    # return render(request, "contractor/contractor.html", {'msg': pk})
