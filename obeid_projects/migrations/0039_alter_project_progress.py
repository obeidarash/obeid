# Generated by Django 3.2.4 on 2021-06-28 10:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obeid_projects', '0038_auto_20210625_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='progress',
            field=models.PositiveIntegerField(default=5, help_text='Pick a number between 0 to 100', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
