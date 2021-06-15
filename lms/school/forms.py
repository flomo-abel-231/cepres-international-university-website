from django import forms
from django.contrib.auth.models import User
from .models import user_profile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=500)
    first_name = forms.CharField(max_length=500)
    last_name = forms.CharField(max_length=500)
    email = forms.EmailField(max_length=500, help_text='Required. Inform a valid email address')

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        labels = {
            "password1": "password",
            "password2": "confirm_password"
        }




class UserProfileForm (forms.ModelForm):
    bio = forms.CharField(required=True)
    student = "student"
    teacher = "teacher"
    parent = "parent"

    user_types = [
        (student, "student"),
        (parent, "parent"),
    ]
    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model = user_profile
        fields = ("bio", "profile_pic", "user_type")

        
