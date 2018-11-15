from django.conf.urls import url
from .views import edit_profile


app_name = 'contractorprofile'
urlpatterns = [

    url(r'^edit-contractor$', edit_profile, name='edit_profile'),


]