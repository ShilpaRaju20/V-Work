from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . models import State



def state(request):
    model_object = State.objects.all()

    if request.method == 'POST':
        form = forms.State_Forms(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('state:State_Forms')
    else:
        form = forms.State_Forms()
    return render(request, 'state/state.html', {'form': form, 'data': model_object})


def edit_state(request, pk):
    template = 'state/state.html'
    post = get_object_or_404(State, pk=pk)
    model_object = State.objects.all()
    if request.method == "POST":
        form = forms.State_Forms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('state:State_Forms')
    else:
        form = forms.State_Forms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_state(request, pk):
    post = get_object_or_404(State, pk=pk)
    post.delete()
    return redirect('state:State_Forms')






