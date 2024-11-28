from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Your Message",initial='Enter your message here...')

class Ordering_form_fields_form(forms.Form):
    name = forms.CharField(label="Full Name")
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(widget=forms.Textarea, label="Message")

    # Reordering fields using the field_order attribute
    field_order = ['email', 'name', 'message']



"""from django import forms

class ContactForm(forms.Form):
    # Name field
    name = forms.CharField(max_length=100, label="Your Name")
    
    # Email field
    email = forms.EmailField(label="Your Email")
    
    # Phone number field
    phone_number = forms.CharField(max_length=15, label="Your Phone Number", required=False)
    
    # Password field
    password = forms.CharField(widget=forms.PasswordInput(), label="Your Password")
    
    # Gender dropdown
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Your Gender")
    
    # Message field
    message = forms.CharField(widget=forms.Textarea, label="Your Message", required=False)
    
    # Age field
    age = forms.IntegerField(label="Your Age", min_value=0, required=False)

    # Checkbox for agreeing to terms
    agree_to_terms = forms.BooleanField(label="I agree to the terms and conditions", required=True)

    # File upload field
    file_upload = forms.FileField(label="Upload a file", required=False)

    # Date of birth field
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.SelectDateWidget(years=range(1900, 2023)))"""
















