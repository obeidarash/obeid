# Generated by Django 3.2.4 on 2021-06-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obeid_projects', '0032_alter_project_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='datetime',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]
