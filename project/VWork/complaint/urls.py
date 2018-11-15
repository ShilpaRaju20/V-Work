from django.conf.urls import url
from .views import complaint

app_name = 'complaint'

urlpatterns = [url(r'^$', complaint, name='Complaint_Forms')]
