# Generated by Django 5.1.4 on 2025-01-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_remove_supplement_slug_remove_supplement_usage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplement',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
