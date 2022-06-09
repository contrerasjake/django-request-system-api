# Generated by Django 4.0.5 on 2022-06-09 16:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0005_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_pic',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]