# Generated by Django 5.1.4 on 2025-01-15 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_foodprogram_remove_comment_supplement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='date',
        ),
    ]
