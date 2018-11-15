from django.conf.urls import url
from .views import works


app_name = 'works'
urlpatterns = [
    url(r'^$', works, name='Work_Forms'),
]