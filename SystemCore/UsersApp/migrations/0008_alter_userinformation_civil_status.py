# Generated by Django 3.2.3 on 2021-06-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0007_alter_userinformation_civil_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='civil_status',
            field=models.CharField(choices=[('Ma', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], max_length=10, null=True),
        ),
    ]
