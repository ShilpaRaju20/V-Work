from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Feedback


def feedback(request):
    login_id = request.session['logid']
    modelobject = Feedback.objects.filter(cust_id=login_id)
    if request.method == 'POST':
        form = forms.Feedback_Forms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.cleaned_data
            conname = obj["con_name"]
            wcategory = obj["work_categoryname"]
            fdates = obj["fdate"]
            desc = obj["feedback"]

            a = Feedback(cust_id=login_id, con_name=conname, work_categoryname=wcategory, fdate=fdates, feedback=desc)
            a.save()
            return redirect('feedback:Feedback_Forms')

    else:
        form = forms.Feedback_Forms
    return render(request, "feedback/feedback.html", {'form': form, 'data': modelobject})


def edit_feedback(request, pk):
    template = 'feedback/feedback.html'
    post = get_object_or_404(Feedback, pk=pk)
    model_object = Feedback.objects.all()
    if request.method == "POST":
        form = forms.Feedback_Forms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('feedback:Feedback_Forms')
    else:
        form = forms.Feedback_Forms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_feedback(request, pk):
    post = get_object_or_404(Feedback, pk=pk)
    post.delete()
    return redirect('feedback:Feedback_Forms')