from django import forms 
from django.contrib.auth.forms import UserCreationForm  # Import the base form
from django.contrib.auth.models import User  # Import the User model
from django.core.exceptions import ValidationError


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
    
    
#type1 reg with email/phone and pass
class CustomUserCreationForm(UserCreationForm):
    email_or_phone = forms.CharField(
        max_length=100, 
        required=True, 
        label="", 
        widget=forms.TextInput(attrs={
            'placeholder': 'Email or Phone', 
            'class': 'field'
        })
    )
    password = forms.CharField(
        required=True, 
        label="", 
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password', 
            'class': 'pass-key'
        })
    )

    class Meta:
        model = User
        fields = ['email_or_phone', 'password']  # Use your custom fields

    def clean_email_or_phone(self):
        data = self.cleaned_data['email_or_phone']
        if '@' in data:  # Treat as email
            if User.objects.filter(email=data).exists():
                raise ValidationError("Email is already taken!")
        else:  # Treat as phone number
            if User.objects.filter(username=data).exists():
                raise ValidationError("Phone number is already registered!")
        return data

    def save(self, commit=True):
        user = User()  # Create a new user instance
        data = self.cleaned_data['email_or_phone']
        if '@' in data:
            user.email = data
        else:
            user.username = data  # Assuming phone is stored as username

        # Set the password
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user