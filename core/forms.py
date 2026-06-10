import django.forms as forms
import pycountry
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
    COUNTRIES = [(country.alpha_2, country.name) for country in pycountry.countries]
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
    paese = forms.ChoiceField(
        ## fai che di default sia italia, così se non lo selezionano è già impostato
        choices=COUNTRIES,
        initial='IT',
        
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'  # Bootstrap 5 (meglio di form-control)
        })
    )
    phone_number = forms.CharField(

    required=False,

    widget=forms.TextInput(attrs={

        'class': 'form-control',

        'inputmode': 'tel',

        'placeholder': '+39 333 123 4567'

    })

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
