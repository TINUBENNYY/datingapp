from django import forms
from django.forms import ModelForm, Form, TextInput, PasswordInput, CharField,EmailInput, DateInput, Select
from .models import User, UserProfile, EmploymentProfile
from django.contrib.auth.hashers import make_password

class UserCreationForm(ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "gender", "dob", "phone"]

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "phone": forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
       
class LoginFrom(Form):
    username = CharField(
        max_length = 20,
        min_length = 4,
        label = 'Username',
        required = True,
        widget = TextInput({'class': 'form-control'})
    )

    password = CharField(
        max_length = 8,
        min_length = 4,
        label = 'Password',
        required = True,
        widget = PasswordInput({'class': 'form-control'})
    )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'dob', 'hobbies', 'interest', 'smoking_habits', 'drinking_habits', 
                  'qualification', 'profile_pic', 'multiple_images', 'short_reel']
        widgets = {
            "age": forms.NumberInput(attrs={'class': 'form-control'}),
            "dob": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "hobbies": forms.TextInput(attrs={'class': 'form-control'}),
            "interest": forms.TextInput(attrs={'class': 'form-control'}),
            "smoking_habits": forms.TextInput(attrs={'class': 'form-control'}),
            "drinking_habits": forms.TextInput(attrs={'class': 'form-control'}),
        }

class EmploymentProfileForm(forms.ModelForm):
    class Meta:
        model = EmploymentProfile
        fields = ['employment_type', 'company_name', 'designation', 'location', 'job_title', 'expertise_level']
        widgets = {
            'employment_type': forms.RadioSelect,
            'expertise_level': forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company_name'].required = False
        self.fields['designation'].required = False
        self.fields['location'].required = False