# Generated by Django 4.2.1 on 2024-03-30 21:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0013_remove_report_teacher_alter_report_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
