# Generated by Django 3.2.4 on 2021-06-15 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obeid_projects', '0026_auto_20210616_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=256),
        ),
    ]
