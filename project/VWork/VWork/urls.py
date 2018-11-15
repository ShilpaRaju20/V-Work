"""VWork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^contractor/', include('contractor_reg.urls')),
    url(r'^customer/', include('customer_reg.urls')),
    url(r'^contractorlogin/', include('login.urls')),
    url(r'^freelancer/', include('freelancers_reg.urls')),
    url(r'^custlogin/', include('customerlogin.urls')),
    url(r'^employeereg/', include('employees.urls')),
    url(r'^works/', include('works.urls')),
    url(r'^profile/', include('contractorprofile.urls')),
    url(r'^adminlogin/', include('adminlogin.urls')),
    url(r'^category/', include('category.urls')),
    url(r'^states/', include('state.urls')),
    url(r'^contractorcategory/', include('contractorcategory.urls')),
    url(r'^constructingcategory/', include('constructingcategory.urls')),
    url(r'^userworks/', include('userworks.urls')),
    url(r'^needlist/', include('needlist.urls')),
    url(r'^approach/', include('approach.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^viewdetails/', include('viewdetails.urls')),
    url(r'^complaint/', include('complaint.urls')),
    url(r'^feedbackview/', include('feedbackview.urls')),
    url(r'^complaintview/', include('complaintview.urls')),





]


