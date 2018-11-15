# Generated by Django 2.0.7 on 2018-09-01 06:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('works', '0002_works'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='amt',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='works',
            name='images',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='works',
            name='work_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='works',
            name='work_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]