# Generated by Django 4.2.6 on 2023-11-02 08:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_commentreportmodel_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprojectrating',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
