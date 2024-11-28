from django import forms 

class DemowidgetForm(forms.Form):
    
    
    name = forms.CharField (
        max_length=100, label="Your Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name' , 'id':"myid"})
    )
    
    
    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}) ,label="Password"
    )
    
    
    message = forms.CharField(
        label="Your Message",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message here'})
    )
    
    
    
    category = forms.ChoiceField(
        choices=[
            ('', 'Select Category'),
            ('books', 'Books'),
            ('clothes', 'Clothes'),
            ('electronics', 'Electronics'),
        ],
        label="Category",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    
    
    subscribe = forms.BooleanField(
        required=False,
        label="Subscribe to newsletter",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


    male = forms.BooleanField(
        required=False,
        label="Male",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    # Female checkbox
    female = forms.BooleanField(
        required=False,
        label="Female",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    
    
    #radio button
    yes_no = forms.ChoiceField(
    choices=[(True, "Yes"), (False, "No")],
    widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    label="Yes or No"
)
    
    
    
    # File upload field
    upload_file = forms.FileField(
        label="Upload your file",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*,application/pdf'})
    )