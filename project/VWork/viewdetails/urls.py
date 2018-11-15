from django.conf.urls import url
from .views import views
from .view1 import view1


app_name = 'viewdetails'

urlpatterns = [
    url(r'viewdetails/(?P<pk>\d+)/$', views, name='views'),
    url(r'viewdetails/(?P<pk>\d+)/$', view1, name='views'),
    # url(r'^$', views, name="views"),


]