from django.conf.urls import url
from .views import constructcategory
from .views import edit_constructcategory
from .views import delete_constructcategory


app_name = 'constructingcategory'
urlpatterns = [
    url(r'^$', constructcategory, name='ConstructCategory_Forms'),
    url(r'edit_constructcategory/(?P<pk>\d+)/$', edit_constructcategory, name='edit_constructcategory'),
    url(r'delete_constructcategory/(?P<pk>\d+)/$', delete_constructcategory, name='delete_constructcategory'),

]