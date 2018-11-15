from django.conf.urls import url
from .views import login, adminhome


app_name = 'adminlogin'

urlpatterns = [
    url(r'^$', login, name='AdminLogin_Forms'),
    url(r'^adminhome$', adminhome, name='adminhome'),
    # url(r'^centerhome$', centerhome, name='centerhome'),

]