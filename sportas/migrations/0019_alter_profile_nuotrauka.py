# Generated by Django 5.1.4 on 2025-01-14 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_alter_profile_nuotrauka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nuotrauka',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
