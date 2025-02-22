# Generated by Django 5.1.4 on 2025-01-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_remove_supplement_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplement',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='supplement',
            name='review',
        ),
        migrations.AddField(
            model_name='supplement',
            name='dosage',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplement',
            name='servings',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
