# Generated by Django 3.2.4 on 2021-06-14 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obeid_projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='progress',
            field=models.PositiveIntegerField(default=5, max_length=100),
        ),
    ]
