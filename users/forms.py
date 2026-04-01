from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms


class CustomCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {"class": "form-control"}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control'}
        )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'}
        )

        self.fields['password'].widget.attrs.update(
            {'class': 'form-control'}
        )

class CustomChangeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['avatar'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['country'].widget.attrs.update(
            {'class': 'form-control'}
        )

    class Meta:
        model = User
        fields = ('avatar', 'email', 'first_name', 'last_name', 'phone','country')