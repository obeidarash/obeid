# Generated by Django 3.2.4 on 2021-06-14 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obeid_projects', '0004_auto_20210615_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='customer',
        ),
    ]