from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Employee


def employee(request):
    login_id = request.session['logid']
    model_object = Employee.objects.filter(contractorreg_id=login_id)
    if request.method == 'POST':
        form = forms.Employee_Forms(request.POST, request.FILES)
        if form.is_valid():
            Empobj = form.cleaned_data
            name = Empobj['emp_name']
            gender = Empobj['gender']
            email = Empobj['mail_id']
            phno = Empobj['phno']
            aadhar = Empobj['aadharno']
            address = Empobj['address']
            street = Empobj['street']
            city = Empobj['city']
            pin = Empobj['pin']
            district = Empobj['district']
            state = Empobj['state_id']
            contractorcategory = Empobj['contractorcat_id']
            a = Employee(emp_name=name, gender=gender, mail_id=email, phno=phno, aadharno=aadhar, address=address,
                         street=street, city=city, pin=pin, district=district, state_id=state,
                         contractorreg_id=request.session['logid'], contractorcat_id=contractorcategory)
            a.save()
        return redirect('employees:Employee_Forms')
    else:
        form = forms.Employee_Forms
    return render(request, "employeereg/empreg.html", {'form': form, 'data': model_object})


def edit_emp(request, pk):
    template = 'employeereg/empreg.html'
    post = get_object_or_404(Employee, pk=pk)
    model_object = Employee.objects.all()
    if request.method == 'POST':
        form = forms.Employee_Forms(request.POST, instance=post)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('employees:Employee_Forms')
    else:
        form = forms.Employee_Forms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_emp(request, pk):

    post = get_object_or_404(Employee, pk=pk)
    post.delete()
    return redirect('employees:Employee_Forms')

