# Generated by Django 2.0.7 on 2018-11-11 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_remove_feedback_cust_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='fdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
