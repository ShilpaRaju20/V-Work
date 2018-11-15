from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["cust_id", "con_name", "work_categoryname", "fdate", "feedback"]


admin.site.register(Feedback, FeedbackAdmin)
