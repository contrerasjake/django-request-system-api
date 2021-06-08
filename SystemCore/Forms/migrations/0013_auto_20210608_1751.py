# Generated by Django 3.2.3 on 2021-06-08 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0012_auto_20210608_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessclearance',
            name='business_nature',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='businessclearance',
            name='business_owner',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='businessclosure',
            name='business_owner',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='guardianship',
            name='guardian_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunization',
            name='father_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunization',
            name='mother_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indigencyburial',
            name='deceased_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indigencyburial',
            name='deceased_relationship',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indigencyburial',
            name='passed_onto_whom',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indigencyclearance',
            name='passed_onto_whom',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indigencyclearance',
            name='patient_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indigencyclearance',
            name='patient_relationship',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indigencyclearance',
            name='purpose',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='maternalcare',
            name='child_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='parent_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='student_name',
            field=models.TextField(max_length=100),
        ),
    ]
