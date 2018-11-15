# Generated by Django 2.0.7 on 2018-08-21 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('state', '0001_initial'),
        ('contractorcategory', '0001_initial'),
        ('contractor_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contractor_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractor_name', models.CharField(default='', max_length=60)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10)),
                ('mail_id', models.CharField(default='', max_length=20)),
                ('phno', models.CharField(default='', max_length=10)),
                ('aadharno', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=50)),
                ('street', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('district', models.CharField(default='', max_length=20)),
                ('username', models.CharField(default='', max_length=30)),
                ('pswd', models.CharField(default='', max_length=15)),
                ('con_status', models.CharField(default='', max_length=20)),
                ('pin', models.CharField(default='', max_length=6)),
                ('con_categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contractorcategory.ContractorCategory')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='state.State')),
            ],
        ),
    ]
