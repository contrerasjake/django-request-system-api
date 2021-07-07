# Generated by Django 3.2.4 on 2021-07-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0018_auto_20210611_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='id_pic',
            field=models.ImageField(blank=True, null=True, upload_to='id_pic/%Y/%m/%D/'),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profilepic/%Y/%m/%D/'),
        ),
    ]
