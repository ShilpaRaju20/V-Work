from django.conf.urls import url
from .views import category
from .views import edit_category
from .views import delete_category


app_name = 'category'
urlpatterns = [
    url(r'^$', category, name='Category_Forms'),
    url(r'edit_category/(?P<pk>\d+)/$', edit_category, name='edit_category'),
    url(r'delete_category/(?P<pk>\d+)/$', delete_category, name='delete_category'),

]