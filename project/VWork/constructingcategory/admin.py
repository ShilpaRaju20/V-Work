from django.contrib import admin
from .models import ConstructingCategory


class ConstructingCategoryAdmin (admin.ModelAdmin):
    list_display = ["construction_name"]


admin.site.register(ConstructingCategory, ConstructingCategoryAdmin)


