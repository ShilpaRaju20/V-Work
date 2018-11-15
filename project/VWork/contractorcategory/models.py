from django.db import models


class ContractorCategory(models.Model):
    concategoryname = models.CharField(max_length=100, default='')
    concategorydesc = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.concategoryname
