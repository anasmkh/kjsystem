# Generated by Django 4.2.1 on 2024-03-29 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mother', '0010_mother_is_mother'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mother',
            name='is_mother',
        ),
    ]
