# Generated by Django 5.1.4 on 2025-01-15 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_alter_profile_nuotrauka'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplement',
            name='image_url',
        ),
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
            name='slug',
            field=models.SlugField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplement',
            name='usage',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplement',
            name='image',
            field=models.ImageField(default=1, upload_to='supplements/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplement',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('supplement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='web.supplement')),
            ],
        ),
    ]
