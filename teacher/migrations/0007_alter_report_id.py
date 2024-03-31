# Generated by Django 4.2.1 on 2024-03-30 20:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_remove_teacher_is_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
