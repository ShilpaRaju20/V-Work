from django.contrib import admin
from .models import contractor_reg

class Contractor_regAdmin(admin.ModelAdmin):
    list_display = ["contractor_name", "gender", "mail_id", "phno", "aadharno", "address", "street", "city", "pin", "district", "con_status", "con_categoryid", "state_id"]

admin.site.register(contractor_reg,Contractor_regAdmin)
