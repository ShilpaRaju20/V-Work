from django.db import models
from state.models import State
CHOICES = [('male', 'Male'), ('female', 'Female'), ('others', 'Others')]


class Customer_Reg(models.Model):
    cust_name = models.CharField(max_length=30, default='')
    gender = models.CharField(choices=CHOICES, max_length=10)
    cust_mailid = models.CharField(max_length=30, default='')
    cust_phno = models.CharField(max_length=10, default='')
    cust_aadharno = models.CharField(max_length=20, default='')
    cust_address = models.CharField(max_length=50, default='')
    cust_street = models.CharField(max_length=50, default='')
    cust_city = models.CharField(max_length=50, default='')
    cust_pin = models.CharField(max_length=6, default='')
    cust_district = models.CharField(max_length=30, default='')
    cust_uname = models.CharField(max_length=30, default='')
    cust_pswd = models.CharField(max_length=15, default='')
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.cust_name
