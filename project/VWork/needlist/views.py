from django.shortcuts import render
from userworks.models import UserWorks
from customer_reg.models import Customer_Reg


def needs(request):
    userobj = UserWorks.objects.all()

    return render(request, "needs/needs.html", {'data': userobj})
