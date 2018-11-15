from django.contrib import admin
from .models import Approach


class ApproachAdmin(admin.ModelAdmin):
    list_display = ["amt", "cdate"]


admin.site.register(Approach, ApproachAdmin)
