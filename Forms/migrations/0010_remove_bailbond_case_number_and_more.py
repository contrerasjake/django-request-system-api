# Generated by Django 4.0.3 on 2022-04-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0009_alter_voucher_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bailbond',
            name='case_number',
        ),
        migrations.RemoveField(
            model_name='immunization',
            name='birth_weight',
        ),
        migrations.AlterField(
            model_name='cedula',
            name='monthly_income',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='constituentid',
            name='id_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]