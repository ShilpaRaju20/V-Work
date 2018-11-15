from django.contrib import admin
from .models import ContractorCategory

class ConcategoryAdmin (admin.ModelAdmin):
    list_display = ["concategoryname", "concategorydesc"]


admin.site.register(ContractorCategory, ConcategoryAdmin)


