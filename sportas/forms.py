from django import forms
from django.contrib.auth.models import User
from .models import Workout, Meal, Profile, Exercise, FoodProgram, Supplement


class MealForm(forms.Form):
    name = forms.CharField(max_length=100, label='Meal Name')
    calories = forms.IntegerField(label='Calories')
    portions = forms.IntegerField(label='Portions')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "El.paštas"
        self.fields['first_name'].label = "Vardas"
        self.fields['last_name'].label = "Pavardė"
        self.fields['username'].help_text = "Pakeitus username, nepamirškite pasikeist ir jungiantis Jūsų username!"
        self.fields[
            'email'].help_text = "Įsitikinkite, kad suvedėte galiojantį el.paštą, kitu atveju negalėsite susigražinti slaptažodžio!"


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['age']


class DateInput(forms.DateInput):
    input_type = 'date'


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'repetitions']


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'description', 'name']


class MealProgramForm(forms.ModelForm):
    class Meta:
        model = FoodProgram
        fields = ['name', 'description', 'goal']


class SupplementForm(forms.ModelForm):
    class Meta:
        model = Supplement
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
