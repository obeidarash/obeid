# Generated by Django 3.2.4 on 2021-06-14 22:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obeid_projects', '0002_project_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='progress',
            field=models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
