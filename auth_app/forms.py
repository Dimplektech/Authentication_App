from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    """
    Form for registering a new user, extending the default UserCreationForm.
    This form uses Django's built-in User model.
    """
    email = forms.EmailField  # Adding an email field to the form

    class Meta:
        """
        Meta class to specify the model and fields to include in the form.
        Uses the built-in User model.
        """
        model = User   # Specify the built-in user model.
        # Fields to include in the form
        fields = ['username', 'email', 'password1', 'password2']  