# Generated by Django 3.2.4 on 2021-06-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obeid_projects', '0031_auto_20210625_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
