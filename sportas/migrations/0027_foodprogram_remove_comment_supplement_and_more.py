# Generated by Django 5.1.4 on 2025-01-15 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_remove_meal_date_remove_meal_name_remove_meal_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('goal', models.CharField(choices=[('weight_loss', 'Svorio metimas'), ('muscle_gain', 'Raumenų auginimas'), ('healthy_eating', 'Sveika mityba')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='supplement',
        ),
        migrations.DeleteModel(
            name='MealProgram',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='total_calories',
        ),
        migrations.AddField(
            model_name='meal',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meal',
            name='program',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='web.foodprogram'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
