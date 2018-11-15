from django.conf.urls import url
from .views import custlogin, userhome

app_name = 'customerlogin'

urlpatterns = [
    url(r'^$', custlogin, name='Custlogin_Forms'),
    url(r'^userhome$', userhome, name='userhome')
]