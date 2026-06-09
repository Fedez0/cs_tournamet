import django.forms as forms

from .models import User


class UserCreationForm(forms.Form):
    model = User
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class EditProfileForm(forms.Form):
    model = User

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False

    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=False
    )
    paese = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    profile_picture = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False
    )
    steam_url = forms.URLField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )


class UserLoginForm(forms.Form):
    model = User

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    