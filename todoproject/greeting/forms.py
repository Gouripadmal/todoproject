from django import forms
from django.core.validators import validate_email

class RegistrationForm(forms.Form):
    full_name = forms.CharField(
        min_length=5,
        max_length=50
    )

    email = forms.CharField(
        validators=[validate_email]
    )

    password = forms.CharField(
        min_length=8,
        max_length=20
    )