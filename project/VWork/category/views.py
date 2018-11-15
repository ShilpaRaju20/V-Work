from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . models import Category



def category(request):
    model_object = Category.objects.all()

    if request.method == 'POST':
        form = forms.Category_Forms(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('category:Category_Forms')
    else:
        form = forms.Category_Forms()
    return render(request, 'Admin/category.html', {'form': form, 'data': model_object})


def edit_category(request, pk):
    template = 'Admin/category.html'
    post = get_object_or_404(Category, pk=pk)
    model_object = Category.objects.all()
    if request.method == "POST":
        form = forms.Category_Forms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('category:Category_Forms')
    else:
        form = forms.Category_Forms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_category(request, pk):
    post = get_object_or_404(Category, pk=pk)
    post.delete()
    return redirect('category:Category_Forms')





