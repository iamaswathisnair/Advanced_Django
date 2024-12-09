from django import forms 
from . models import User,NewUser


# 1. Create a Base ModelForm
class Userform(forms.ModelForm):
    class Meta:
        model = NewUser
        fields ="__all__"
    
# 2. Create Child ModelForms

class Teacherform(Userform):
     # 3 Inherit Meta from the base form
     class Meta(Userform.Meta):
        fields =  ['name','email','password'] 
        #  fields = Userform.Meta.fields # 4 -- No additional fields
         
class EmployeeForm(Userform):
    class Meta(Userform.Meta):  # Inherit Meta from the base form
        fields =  ['empname','email','password']  # Add 'password' field
        # fields = Userform.Meta.fields + ['password']  # Add 'password' field
        