# Generated by Django 2.0.7 on 2018-09-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractor_reg', '0004_auto_20180924_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor_reg',
            name='confirmpswd',
            field=models.CharField(default='', max_length=15),
        ),
    ]