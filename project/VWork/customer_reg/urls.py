from django.conf.urls import url
from .views import customer

app_name = 'customer_reg'

urlpatterns = [
    url(r'^$', customer, name='Customer_Forms')
]