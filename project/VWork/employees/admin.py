from django.contrib import admin
from .models import Employee


class EmpAdmin(admin.ModelAdmin):
    list_display = ["emp_name", "gender", "mail_id", "phno", "aadharno", "address", "street", "city", "pin", "district", "state_id", "contractorreg_id", "contractorcat_id"]


admin.site.register(Employee, EmpAdmin)


