from django.db import models
from datetime import date
from contractor_reg.models import contractor_reg


class Complaint(models.Model):
    cust_id = models.BigIntegerField()
    contractor_name = models.ForeignKey(contractor_reg, on_delete=models.CASCADE)
    cdate = models.DateField(default=date.today)
    complaint = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.complaint


