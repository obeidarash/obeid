# Generated by Django 3.2.4 on 2021-06-15 21:38

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('obeid_projects', '0024_auto_20210616_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]