# Generated by Django 4.2.1 on 2024-03-20 17:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mother', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mother',
            old_name='full_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='child',
            name='age',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
