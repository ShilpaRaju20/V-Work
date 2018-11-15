from django.conf.urls import url
from .views import contractor

app_name = 'contractor_reg'

urlpatterns = [
    url(r'^$', contractor, name='Contractor_forms')
]