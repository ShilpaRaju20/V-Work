from django.conf.urls import url
from .views import feedback
from .views import edit_feedback
from .views import delete_feedback

app_name = 'feedback'

urlpatterns = [
    url(r'^$', feedback, name='Feedback_Forms'),
    url(r'edit_feedback/(?P<pk>\d+)/$', edit_feedback, name='edit_feedback'),
    url(r'delete_feedback/(?P<pk>\d+)/$', delete_feedback, name='delete_feedback'),
]