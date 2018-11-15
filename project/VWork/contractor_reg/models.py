from django.db import models
from contractorcategory.models import ContractorCategory
from state.models import State
CHOICES = [('male', 'Male'), ('female', 'Female'), ('others', 'Others')]

class contractor_reg(models.Model):
    contractor_name = models.CharField(max_length=60, default='')
    gender = models.CharField(choices=CHOICES, max_length=10)
    mail_id = models.CharField(max_length=70, default='')
    phno = models.CharField(max_length=10, default='')
    aadharno = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=50, default='')
    street = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    pin = models.CharField(max_length=6, default='')
    district = models.CharField(max_length=20, default='')
    username = models.CharField(max_length=30, default='')
    pswd = models.CharField(max_length=15, default='')
    con_status = models.BigIntegerField(default='0')
    con_categoryid = models.ForeignKey(ContractorCategory, on_delete=models.CASCADE)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)



    def __str__(self):
        return self.contractor_name