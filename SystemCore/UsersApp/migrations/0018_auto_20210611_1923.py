# Generated by Django 3.2.4 on 2021-06-11 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0017_auto_20210611_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='userinformation',
            name='FirstName',
        ),
        migrations.RemoveField(
            model_name='userinformation',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='userinformation',
            name='UserName',
        ),
    ]
