# Generated by Django 3.2.4 on 2021-06-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obeid_projects', '0022_project_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]