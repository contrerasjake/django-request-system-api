# Generated by Django 4.0.3 on 2022-03-22 05:48

import UsersApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_pic',
            field=models.ImageField(blank=True, null=True, upload_to=UsersApp.models.upload_idpic),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=UsersApp.models.upload_profilepic),
        ),
    ]
