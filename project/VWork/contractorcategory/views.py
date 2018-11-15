from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . models import ContractorCategory



def constructcategory(request):
    model_object = ContractorCategory.objects.all()

    if request.method == 'POST':
        form = forms.ConCategory_Forms(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('contractorcategory:ConCategory_Forms')
    else:
        form = forms.ConCategory_Forms()
    return render(request, 'contractorcategory/contractorcategory.html', {'form': form, 'data': model_object})


def edit_concategory(request, pk):
    template = 'contractorcategory/contractorcategory.html'
    post = get_object_or_404(ContractorCategory, pk=pk)
    model_object = ContractorCategory.objects.all()
    if request.method == "POST":
        form = forms.ConCategory_Forms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('contractorcategory:ConCategory_Forms')
    else:
        form = forms.ConCategory_Forms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_concategory(request, pk):
    post = get_object_or_404(ContractorCategory, pk=pk)
    post.delete()
    return redirect('contractorcategory:ConCategory_Forms')





