from django.shortcuts import render,redirect
from . import forms
from .models import Works

def works(request):
    login_id = request.session['logid']
    model_object = Works.objects.filter(contractor_id=login_id)
    if request.method == 'POST':
        form = forms.Work_Forms(request.POST, request.FILES)
        if form.is_valid():
            Workobj = form.cleaned_data
            wname = Workobj['work_name']
            constructcat = Workobj['constructioncat_id']
            wdate = Workobj['work_date']
            amt = Workobj['amt']
            image = Workobj['images']

            work = Works(work_name=wname, constructioncat_id=constructcat, work_date=wdate, amt=amt, images=image, contractor_id=request.session['logid'])
            work.save()
        return redirect('works:Work_Forms')
    else:
        form = forms.Work_Forms
    return render(request, "workdetails/work.html", {'form': form, 'data': model_object})
