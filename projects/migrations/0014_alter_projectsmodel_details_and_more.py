# Generated by Django 4.2.7 on 2024-01-17 02:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_alter_projectsmodel_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsmodel',
            name='details',
            field=models.TextField(max_length=3000, validators=[django.core.validators.MinLengthValidator(50)]),
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
