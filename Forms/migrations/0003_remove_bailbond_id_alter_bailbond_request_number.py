# Generated by Django 4.0.3 on 2022-04-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bailbond',
            name='id',
        ),
        migrations.AlterField(
            model_name='bailbond',
            name='request_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
