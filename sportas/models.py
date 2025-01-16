from operator import truediv
from django.contrib.auth.models import User
from django.db import models


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    name = models.CharField(max_length=100, null=True, blank=True)
    duration = models.IntegerField()

    def formatted_date(self):
        return self.date.strftime('%Y-%m-%d')

    formatted_date.short_description = 'Date'

    def __str__(self):
        return self.title


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    repetitions = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Supplement(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    servings = models.IntegerField()
    dosage = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class FoodProgram(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    goal = models.CharField(max_length=50, choices=[
        ('weight_loss', 'Svorio metimas'),
        ('muscle_gain', 'Raumenų auginimas'),
        ('healthy_eating', 'Sveika mityba')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Meal(models.Model):
    program = models.ForeignKey(FoodProgram, related_name='meals', on_delete=models.CASCADE)
    meal_name = models.CharField(max_length=100)
    calories = models.FloatField()
    portions = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.meal_name
