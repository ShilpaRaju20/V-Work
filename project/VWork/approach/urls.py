from django.conf.urls import url
from .views import approach

app_name = 'approach'

urlpatterns = [
    url(r'approach/(?P<pk>\d+)/$', approach, name='Approach_Forms')
]
