# Generated by Django 2.0.7 on 2018-10-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approach', '0005_approach_empname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approach',
            name='empavail',
        ),
        migrations.RemoveField(
            model_name='approach',
            name='empname',
        ),
        migrations.AddField(
            model_name='approach',
            name='work_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]