from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='main'),
    path("workouts/<str:category>/", views.workout_details, name="workout_details"),
    path('workouts/', views.workouts, name='workouts'),
    path('meals/', views.meals, name='meals'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('main/', views.profilis2, name='main'),
    path('paieska/', views.paieska, name='paieska'),
    path('calorie-calculator/', views.calorie_calculator, name='calorie_calculator'),
    path('supplement_list/', views.supplement_list, name='supplement_list'),
    path('supplements/<int:id>/', views.supplement_detail, name='supplement_detail'),
    path('meal/<int:pk>/', views.meals, name='meal_detail'),


]
