from django.shortcuts import render,redirect
from . import forms
from contractor_reg.models import contractor_reg


def userhome(request):
    return render(request, 'Homepage/home.html', {'logidd': request.session['logid']})


def login(request):
    if request.method == 'POST':
        form = forms.Login_Forms(request.POST)
        if form.is_valid():
            userobj = form.cleaned_data
            username = userobj['username']
            password = userobj['password']
            if contractor_reg.objects.filter(username=username).exists() and contractor_reg.objects.filter(pswd=password).exists():
                obj = contractor_reg.objects.get(username=username)

                request.session['logid'] = obj.id
                return redirect('login:userhome')
            else:
                return render(request, 'login/login.html', {'form': form})

    else:
        form = forms.Login_Forms()
    return render(request, 'login/login.html', {'form': form})