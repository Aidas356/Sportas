# Generated by Django 5.1.4 on 2025-01-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_mealprogram_alter_meal_calories_alter_meal_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='NutritionPlan',
        ),
    ]
