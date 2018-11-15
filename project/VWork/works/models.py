from django.db import models
from contractor_reg.models import contractor_reg
from constructingcategory.models import ConstructingCategory
from datetime import date


class Works(models.Model):
    work_name = models.CharField(max_length=80, default='')
    contractor_id = models.BigIntegerField()
    constructioncat_id = models.ForeignKey(ConstructingCategory, on_delete=models.CASCADE)
    work_date = models.DateField(default=date.today)
    amt = models.CharField(max_length=10, default='')
    images = models.ImageField()


    def __str__(self):
        return self.work_name
