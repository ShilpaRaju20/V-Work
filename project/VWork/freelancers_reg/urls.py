from django.conf.urls import url
from .views import freelancer

app_name = 'freelancers_reg'

urlpatterns = [
    url(r'^$', freelancer, name='Freelancer_Forms')
]