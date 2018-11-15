from django.shortcuts import render, redirect
from . import forms
from .models import Freelancers_Reg


def freelancer(request):
    if request.method == 'POST':
        form = forms.Freelancer_Forms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            msg = "Successfully Inserted"
            return redirect('freelancers_reg:Freelancer_Forms')
    else:
        form = forms.Freelancer_Forms
        msg = "Unsuccessful"

    return render(request, "freelancerreg/freelancerreg.html", {'form': form, 'msg': msg})
