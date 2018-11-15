from django.db import models
from category.models import Category
CHOICES = [('male', 'Male'), ('female', 'Female'), ('others', 'Others')]

class Freelancers_Reg(models.Model):
    name = models.CharField(max_length=30, default='')
    gender = models.CharField(choices=CHOICES, max_length=10)
    mail_id = models.CharField(max_length=30, default='')
    phno = models.CharField(max_length=10, default='')
    aadhar_no = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=50, default='')
    street = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    pin = models.CharField(max_length=6, default='')
    district = models.CharField(max_length=20, default='')
    work_categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    freelancer_status = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name
