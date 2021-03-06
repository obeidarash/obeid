# Generated by Django 3.2.4 on 2021-06-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obeid_projects', '0028_customer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=models.SlugField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=256, unique=True),
        ),
    ]
