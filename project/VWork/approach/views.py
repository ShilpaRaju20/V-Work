from django.shortcuts import render, redirect
from . import forms
from userworks.models import UserWorks
from approach.models import Approach
from contractor_reg.models import contractor_reg


def approach(request, pk):
    login_id = request.session['logid']
    modelobject = UserWorks.objects.get(id=pk)
    modelobject1 = UserWorks.objects.filter(id=pk)
    if request.method == 'POST':
        form = forms.Approach_Forms(request.POST, request.FILES)
        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.save()
            obj = form.cleaned_data
            cid = modelobject.cust_id
            cname = modelobject.custname
            famt = obj["amt"]
            fdate = obj["cdate"]
            a = Approach(con_id=login_id, amt=famt, cdate=fdate, cust_id=cid, custname=cname, work_id=pk)
            a.save()

            return redirect('needlist:needs')
    else:
        form = forms.Approach_Forms()
    return render(request, 'approach/approach.html', {'form': form, 'data': modelobject1})
    # return render(request, 'approach/approach.html', {'form': form})
