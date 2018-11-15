from django.contrib import admin
from .models import Freelancers_Assign

class FreelancersAssignAdmin(admin.ModelAdmin):
    list_display = ["assign_date", "contractor_id", "freelancer_id", "userwork_id"]


admin.site.register(Freelancers_Assign, FreelancersAssignAdmin)
