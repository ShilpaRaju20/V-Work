from django.db import models
from contractor_reg.models import contractor_reg
from datetime import date
from category.models import Category


class Feedback(models.Model):
    cust_id = models.BigIntegerField()
    # cust_name = models.ForeignKey(Customer_Reg, on_delete=models.CASCADE)
    con_name = models.ForeignKey(contractor_reg, on_delete=models.CASCADE)
    work_categoryname = models.ForeignKey(Category, on_delete=models.CASCADE)
    fdate = models.DateField(default=date.today)
    feedback = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.feedback

