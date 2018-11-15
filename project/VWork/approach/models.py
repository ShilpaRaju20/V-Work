from django.db import models
from datetime import date


class Approach(models.Model):
    work_id = models.BigIntegerField()
    con_id = models.BigIntegerField()
    cust_id = models.BigIntegerField()
    custname = models.CharField(max_length=30, default='')
    amt = models.CharField(max_length=10, default='')
    cdate = models.DateField(default=date.today)

    def __str__(self):
        return self.amt

