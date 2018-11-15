from django.conf.urls import url
from .views import views

app_name = 'viewdetails'

urlpatterns = [
    url(r'viewdetails/(?P<pk>\d+)/$', views, name='views'),
    # url(r'approach/(?P<pk>\d+)/$', approach, name='Approach_Forms')
]