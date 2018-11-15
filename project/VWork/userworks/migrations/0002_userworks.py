# Generated by Django 2.0.7 on 2018-08-21 09:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer_reg', '0001_initial'),
        ('category', '0001_initial'),
        ('userworks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userwork_date', models.DateField(default=datetime.date.today)),
                ('work_plot', models.CharField(default='', max_length=50)),
                ('work_amt', models.CharField(default='', max_length=6)),
                ('status', models.CharField(choices=[('booked', 'Booked'), ('pending', 'Pending')], max_length=10)),
                ('cust_regid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_reg.Customer_Reg')),
                ('work_categoryname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
            ],
        ),
    ]