from django.shortcuts import render, redirect
from . import forms
from .models import UserWorks
from customer_reg.models import Customer_Reg


def userwrk(request):
    login_id = request.session['logid']
    modelobject = UserWorks.objects.filter(cust_id=login_id)
    custobj = Customer_Reg.objects.get(id=login_id)
    if request.method == 'POST':
        form = forms.UserWork_Forms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.cleaned_data
            custname = custobj.cust_name
            custphno = custobj. cust_phno
            custemail = custobj.cust_mailid
            wrkkdate = obj["userwork_date"]
            wrkplot = obj["work_plot"]
            work_categoryname = obj["work_categoryname"]

            a = UserWorks(custname=custname, custphno=custphno, custemail=custemail, userwork_date=wrkkdate, work_plot=wrkplot, work_categoryname=work_categoryname, cust_id=request.session['logid'])
            a.save()

            return redirect('userworks:UserWork_Forms')
    else:
        form = forms.UserWork_Forms
        msg = "Unsuccessful"
    return render(request, "userwrks/userwork.html", {'form': form, 'msg': msg})
