# Generated by Django 2.0.7 on 2018-08-21 09:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('freelancers_reg', '0001_initial'),
        ('contractor_reg', '0002_contractor_reg'),
        ('userworks', '0002_userworks'),
        ('freelancers_assign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Freelancers_Assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_date', models.DateField(default=datetime.date.today)),
                ('contractor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contractor_reg.contractor_reg')),
                ('freelancer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancers_reg.Freelancers_Reg')),
                ('userwork_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userworks.UserWorks')),
            ],
        ),
    ]
