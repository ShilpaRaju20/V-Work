from django.contrib import admin
from .models import UserWorks

class UserwrkAdmin(admin.ModelAdmin):
    list_display = ["userwork_date", "work_plot", "work_categoryname", "status"]


admin.site.register(UserWorks, UserwrkAdmin)



