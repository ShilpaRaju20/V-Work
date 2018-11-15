from django.conf.urls import url
from .views import feedbacks

app_name = 'feedbackview'

urlpatterns = [
    url(r'^$', feedbacks, name="feedbacks"),
]