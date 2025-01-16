# Generated by Django 5.1.4 on 2025-01-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_remove_profile_profile_picture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AlterField(
            model_name='profile',
            name='nuotrauka',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
