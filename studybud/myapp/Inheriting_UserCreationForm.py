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
    # Modifying the built-in form to accept email or phone instead of username.
    email_or_phone = forms.CharField(
        max_length=100,
        required=True,
        label="Email or Phone",
        widget=forms.TextInput(attrs={'placeholder': 'Email or Phone', 'class': 'field'})
    )

    # Meta class to define which model this form corresponds to.
    class Meta:
        model = User  # Default User model
        fields = ['email_or_phone', 'password1', 'password2']  # We can still use password1 and password2 as default

    def clean_email_or_phone(self):
        # Check if email_or_phone is already taken
        email_or_phone = self.cleaned_data['email_or_phone']
        if User.objects.filter(username=email_or_phone).exists():
            raise ValidationError("This email or phone number is already taken.")
        return email_or_phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email_or_phone']  # Set email_or_phone as the username
        if commit:
            user.save()
        return user