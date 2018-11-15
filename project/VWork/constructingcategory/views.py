from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . models import ConstructingCategory



def constructcategory(request):
    model_object = ConstructingCategory.objects.all()

    if request.method == 'POST':
        form = forms.ConstructCategory_Forms(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('constructingcategory:ConstructCategory_Forms')
    else:
        form = forms.ConstructCategory_Forms()
    return render(request, 'constructingcategory/constructingcategory.html', {'form': form, 'data': model_object})


def edit_constructcategory(request, pk):
    template = 'constructingcategory/constructingcategory.html'
    post = get_object_or_404(ConstructingCategory, pk=pk)
    model_object = ConstructingCategory.objects.all()
    if request.method == "POST":
        form = forms.ConstructCategory_Forms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('constructingcategory:ConstructCategory_Forms')
    else:
        form = forms.ConstructCategory_Forms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_constructcategory(request, pk):
    post = get_object_or_404(ConstructingCategory, pk=pk)
    post.delete()
    return redirect('constructingcategory:ConstructCategory_Forms')






