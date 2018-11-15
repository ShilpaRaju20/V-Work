from django.conf.urls import url
from .views import employee,edit_emp, delete_emp


app_name = 'employees'
urlpatterns = [
    url(r'^$', employee, name='Employee_Forms'),
    url(r'^edit-employee/(?P<pk>\d+)/$', edit_emp, name='edit_emp'),
    url(r'^delete-employee/(?P<pk>\d+)/$', delete_emp, name='delete_emp'),


]