from django.conf.urls import url
from .views import login, userhome

app_name = 'login'

urlpatterns = [
    url(r'^$', login, name='Login_Forms'),
    url(r'^userhome$', userhome, name='userhome')
]