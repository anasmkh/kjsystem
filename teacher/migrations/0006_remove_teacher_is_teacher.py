# Generated by Django 4.2.1 on 2024-03-30 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_report_child_teacher_is_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='is_teacher',
        ),
    ]
