# Generated by Django 5.1.4 on 2025-01-14 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_delete_yourmodel_supplement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
