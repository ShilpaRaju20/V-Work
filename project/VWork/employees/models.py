from django.db import models
from state.models import State
from contractorcategory.models import ContractorCategory

CHOICES = [('male', 'Male'), ('female', 'Female'), ('others', 'Others')]


class Employee(models.Model):
    emp_name = models.CharField(max_length=60, default='')
    gender = models.CharField(choices=CHOICES, max_length=10)
    mail_id = models.CharField(max_length=20, default='')
    phno = models.CharField(max_length=10, default='')
    aadharno = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=50, default='')
    street = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    pin = models.CharField(max_length=6, default='')
    district = models.CharField(max_length=20, default='')
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    contractorreg_id = models.BigIntegerField()
    contractorcat_id = models.ForeignKey(ContractorCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name

