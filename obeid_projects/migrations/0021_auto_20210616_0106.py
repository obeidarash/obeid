# Generated by Django 3.2.4 on 2021-06-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obeid_projects', '0020_auto_20210615_1727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='obeid_projects.Category', verbose_name='Categories'),
        ),
    ]
