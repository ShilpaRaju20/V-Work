from django.contrib import admin
from .models import Works


class WorkAdmin(admin.ModelAdmin):
    list_display = ["work_name", "contractor_id", "constructioncat_id", "work_date", "amt", "images"]


admin.site.register(Works, WorkAdmin)
