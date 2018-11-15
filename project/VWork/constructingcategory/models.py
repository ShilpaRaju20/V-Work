from django.db import models


class ConstructingCategory(models.Model):
    construction_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.construction_name
