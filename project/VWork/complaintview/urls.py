from django.conf.urls import url
from .views import complaints

app_name = 'complaintview'

urlpatterns = [
    url(r'^$', complaints, name="complaints"),
]