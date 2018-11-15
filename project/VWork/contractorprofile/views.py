from django.shortcuts import render, redirect
from . import forms
from contractor_reg.models import contractor_reg

def edit_profile(request):
    template = 'contractorprofiles/profile.html'
    post = contractor_reg.objects.get(id=request.session['logid'])

    if request.method == 'POST':
        form = forms.Profile_Forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('contractorprofile:edit_profile')
    else:
        form = forms.Profile_Forms(instance=post)
        context = {
            'form': form,
            'post': post,

        }
    return render(request, template, context)
