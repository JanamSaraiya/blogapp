from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = forms.ChoiceField(choices=choices, required=False)
    age = forms.IntegerField(required=False)
    facebook = forms.CharField(max_length=100, required=False)
    insta = forms.CharField(max_length=100, required=False)
    linkedin = forms.CharField(max_length=100, required=False)
    twitter = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Profile
        fields = ['profile_img', 'age', 'gender',
                  'facebook', 'insta', 'linkedin', 'twitter']
