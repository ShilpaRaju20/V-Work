from django.contrib import admin
from .models import Customer_Reg

class Customer_regAdmin(admin.ModelAdmin):
    list_display = ["cust_name", "gender", "cust_mailid",  "cust_phno", "cust_aadharno", "cust_address", "cust_street", "cust_city", "cust_pin", "cust_district", "cust_uname", "state_id"]


admin.site.register(Customer_Reg, Customer_regAdmin)


