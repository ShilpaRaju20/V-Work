from django.contrib import admin
from .models import Freelancers_Reg


class FreelancerAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "mail_id", "phno", "aadhar_no", "address", "street", "city", "pin", "district", "work_categoryid", "freelancer_status"]


admin.site.register(Freelancers_Reg, FreelancerAdmin)