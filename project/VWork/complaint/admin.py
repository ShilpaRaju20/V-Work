from django.contrib import admin
from .models import Complaint

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['cust_id', 'contractor_name', 'cdate', 'complaint']


admin.site.register(Complaint, ComplaintAdmin)

