from django.conf.urls import url
from .views import state
from .views import edit_state
from .views import delete_state


app_name = 'state'
urlpatterns = [
    url(r'^$', state, name='State_Forms'),
    url(r'edit_state/(?P<pk>\d+)/$', edit_state, name='edit_state'),
    url(r'delete_state/(?P<pk>\d+)/$', delete_state, name='delete_state'),

]