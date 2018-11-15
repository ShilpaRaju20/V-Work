from django.shortcuts import render, redirect
from .import forms
from .models import Complaint

def complaint(request):
    login_id = request.session['logid']
    modelobject = Complaint.objects.filter(cust_id=login_id)
    if request.method == 'POST':
        form = forms.Complaint_Forms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.cleaned_data
            conname = obj["contractor_name"]
            cdates = obj["cdate"]
            com = obj["complaint"]
            a = Complaint(cust_id=login_id, contractor_name=conname, cdate=cdates, complaint=com)
            a.save()
            return redirect('complaint:Complaint_Forms')

    else:
        form = forms.Complaint_Forms
    return render(request, "complaint/complaint.html", {'form': form, 'data': modelobject})

