# Generated by Django 4.0.3 on 2022-03-13 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_url_table_creation_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_table',
            name='creation_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
