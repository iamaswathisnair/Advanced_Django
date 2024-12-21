from django import forms 
from django.contrib.auth.forms import UserCreationForm  # Import the base form
from django.contrib.auth.models import User  # Import the User model


# Even though UserCreationForm is being imported 
# (and it already provides the basic functionality for user registration), 
# you often need django.forms for the following reasons:

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False , help_text="Optional.")  # This requires forms.CharField
    date_of_birth = forms.DateField(required=False)  # This requires forms.DateField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'date_of_birth']
        labels = {
            'username': 'Username',
            'email': 'Emailll',
            'password1': 'Password',
            'password2': 'Password Confirmation',
            'phone_number': 'Phone BRO',
            'date_of_birth': 'DOB',
        }
        
        
