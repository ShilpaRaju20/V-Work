from django.shortcuts import render, redirect
from . import forms
from customer_reg.models import Customer_Reg


def userhome(request):
    return render(request, 'CustomerHomePage/home.html', {'logidd': request.session['logid']})


def custlogin(request):
    if request.method == 'POST':
        form = forms.Custlogin_Forms(request.POST)
        if form.is_valid():
            userobj = form.cleaned_data
            username = userobj['username']
            password = userobj['password']
            if Customer_Reg.objects.filter(cust_uname=username).exists() and Customer_Reg.objects.filter(
                    cust_pswd=password).exists():
                obj = Customer_Reg.objects.get(cust_uname=username)

                request.session['logid'] = obj.id
                return redirect('customerlogin:userhome')
            else:
                return render(request, 'customerlogin/login.html', {'form': form})

    else:
        form = forms.Custlogin_Forms()
    return render(request, 'customerlogin/login.html', {'form': form})
