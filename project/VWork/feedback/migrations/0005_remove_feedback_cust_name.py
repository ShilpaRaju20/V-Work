# Generated by Django 2.0.7 on 2018-11-10 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_feedback_cust_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='cust_name',
        ),
    ]