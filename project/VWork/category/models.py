from django.db import models


class Category(models.Model):
    categoryname = models.CharField(max_length=70, default='')

    def __str__(self):
        return self.categoryname

