# Generated by Django 2.0.7 on 2018-10-06 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contractor_reg', '0005_contractor_reg_confirmpswd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractor_reg',
            name='confirmpswd',
        ),
    ]
