# Generated by Django 4.2.6 on 2023-10-26 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsmodel',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
