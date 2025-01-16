from django.contrib import admin
from .models import Workout, Exercise, Meal, Profile, FoodProgram


class WorkoutInline(admin.TabularInline):
    model = Workout
    extra = 1
    can_delete = False


class MealInline(admin.TabularInline):
    model = Meal
    extra = 1


class FoodProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'goal', 'created_at')
    inlines = [MealInline]


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'duration', 'description')
    search_fields = ('title', 'user__username')
    fieldsets = (
        ('Workout Details', {
            'fields': ('title', 'description', 'duration')
        }),
        ('User Info', {
            'fields': ('user',)}),
    )


class MealAdmin(admin.ModelAdmin):
    list_display = ('meal_name', 'calories', 'portions', 'program')
    search_fields = ('meal_name',)


class FoodProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'goal', 'created_at')
    search_fields = ('name', 'goal')


class NutritionPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'total_calories')
    search_fields = ('title', 'user__username')
    fieldsets = (
        ('Plan Details', {
            'fields': ('title', 'description', 'total_calories', 'file')
        }),
        ('User Info', {
            'fields': ('user',)}),
    )


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(FoodProgram, FoodProgramAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Profile)
admin.site.register(Exercise)
