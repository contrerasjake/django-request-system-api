# Generated by Django 3.2.3 on 2021-06-08 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0003_auto_20210529_2133'),
        ('Forms', '0016_alter_cedula_resident_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cedula',
            name='resident_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UsersApp.userinformation'),
        ),
    ]
