from django.conf.urls import url
from .views import constructcategory
from .views import edit_concategory
from .views import delete_concategory


app_name = 'contractorcategory'
urlpatterns = [
    url(r'^$', constructcategory, name='ConCategory_Forms'),
    url(r'edit_concategory/(?P<pk>\d+)/$', edit_concategory, name='edit_concategory'),
    url(r'delete_concategory/(?P<pk>\d+)/$', delete_concategory, name='delete_concategory'),

]