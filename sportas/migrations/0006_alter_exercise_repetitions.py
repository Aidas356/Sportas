# Generated by Django 5.1.4 on 2025-01-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_exercise_repetitions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='repetitions',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
