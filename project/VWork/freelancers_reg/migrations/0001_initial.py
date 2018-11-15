# Generated by Django 2.0.7 on 2018-08-21 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Freelancers_Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10)),
                ('mail_id', models.CharField(default='', max_length=30)),
                ('phno', models.CharField(default='', max_length=10)),
                ('aadhar_no', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=50)),
                ('street', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('pin', models.CharField(default='', max_length=6)),
                ('district', models.CharField(default='', max_length=20)),
                ('work_categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
            ],
        ),
    ]
