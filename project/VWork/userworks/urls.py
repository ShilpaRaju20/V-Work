from django.conf.urls import url
from .views import userwrk

app_name = 'userworks'

urlpatterns = [
    url(r'^$', userwrk, name='UserWork_Forms')
]