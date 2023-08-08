from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm
from django import forms

from catalog_app.forms import StyleFormMixin
from users_app.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'country', 'avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class CustomPasswordResetForm(StyleFormMixin, PasswordResetForm):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User


class CustomResetConfirmForm(StyleFormMixin, SetPasswordForm):
    class Meta:
        model = User
