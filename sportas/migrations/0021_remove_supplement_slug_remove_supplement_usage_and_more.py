# Generated by Django 5.1.4 on 2025-01-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_remove_supplement_image_url_remove_supplement_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplement',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='supplement',
            name='usage',
        ),
        migrations.AddField(
            model_name='supplement',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplement',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='supplement',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='supplements/'),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
