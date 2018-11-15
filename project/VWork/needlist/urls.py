from django.conf.urls import url
from .views import needs

app_name = 'needlist'

urlpatterns = [
    url(r'^$', needs, name="needs"),
]