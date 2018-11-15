from django.db import models
from datetime import date
from contractor_reg.models import contractor_reg
from freelancers_reg.models import Freelancers_Reg
from userworks.models import UserWorks
from datetime import date


class Freelancers_Assign(models.Model):
    assign_date = models.DateField(default=date.today)
    contractor_id = models.ForeignKey(contractor_reg, on_delete=models.CASCADE)
    freelancer_id = models.ForeignKey(Freelancers_Reg, on_delete=models.CASCADE)
    userwork_id = models.ForeignKey(UserWorks, on_delete=models.CASCADE)

    def __str__(self):
        return self.contractor_id

