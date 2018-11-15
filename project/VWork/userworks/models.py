from django.db import models
from customer_reg.models import Customer_Reg
from category.models import Category
from datetime import date
CHOICES = [('booked', 'Booked'), ('pending', 'Pending')]


class UserWorks(models.Model):
    cust_id = models.BigIntegerField()
    custname = models.CharField(max_length=30, default='')
    custphno = models.CharField(max_length=10, default='')
    custemail = models.CharField(max_length=30, default='')
    userwork_date = models.DateField(default=date.today)
    work_plot = models.CharField(max_length=50, default='')
    work_categoryname = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(choices=CHOICES, max_length=10)

    def __str__(self):
        return self.work_plot


