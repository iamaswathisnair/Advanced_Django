from django.shortcuts import render , HttpResponseRedirect
from django.http import HttpResponse
from datetime import datetime , date 
from .forms import ContactForm , Ordering_form_fields_form ,Userform
from .form_widgets import DemowidgetForm
from .modelform_inheritance import EmployeeForm ,Teacherform
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . Inheriting_UserCreationForm import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def learn_django(request):  #request: Represents the HTTP request sent by the client (e.g., a browser).
    d=datetime.now()  #datetime.now() for the full date and time.
    d1=date.today() # from the datetime module for just the current date.
    return render (request , 'index.html' , {'name':"achu","da":d,"da2":d1}) 

def learn_tags(request):
    return render (request , 'if_tags.html' , {'name':False}) 

def oper_tags(request):
    return render (request , 'if_tags.html' , {'name':'aswathi','age':23}) 

def for_tags(request):
    fruits = ["achu","apple","banana","cherry","crispo"]
    return render(request, 'for_tags.html', {'fruits': fruits})

def for_static(request):
    return render (request , 'for_static.html' , {'name':'Aswathi s nair'}) 


def temp_inheritance(request):
    return render (request , 'base.html') 

def about(request):
    return render (request , 'about.html') 

def contact(request):
    return render (request , 'contact.html') 

def for_urls(request):
    return render (request , 'for_urls.html') 

def include_tag(request):
    return render (request , 'the_include_tag.html') 

def contact_view(request):
    form = ContactForm()
    return render (request , 'contact_form.html',{'form':form})

def Ordering_form_fields_view(request):
    form = Ordering_form_fields_form()
    return render (request , 'Ordering_form_fields.html',{'form':form})

# widget form view 

def DemowidgetForm_view(request):
    form = DemowidgetForm()
    return render(request , 'widgetform_loading.html',{'form':form})


                        #modelformview meta

def usermodelform(request):
    fm=Userform()
    return render (request ,'user_modelform.html' , {'form': fm})

                        #model inheritance view 
                        
def teacher_model_inheritance(request):
    if request.method =="POST":
        formm =Teacherform(request.POST)
        if formm.is_valid():
            formm.save()
    else:
        formm =Teacherform()
    return render(request, "Tchr_modelinheritance.html",{'form':formm})


def emp_model_inheritence(request):
    if request.method == "POST":
       formm = EmployeeForm(request.POST)
       if formm.is_valid():
           formm.save()
           messages.success(request, 'Your action was successful!')
    else:
        formm = EmployeeForm()
    return render(request, "emp_modelinheritance_form.html", {'form':formm})
    


#reg using django built-in usercreationform

def user_reg(request):
    if request.method == 'POST':
     formm =UserCreationForm(request.POST)
     if formm.is_valid():
         formm.save()
    else:
        formm = UserCreationForm()
    return render(request ,'user_reg.html' , {'fm':formm})


#inheriting UserCreation form to add more fields 

def register(request):
    if request.method == 'POST':
       form = CustomUserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, 'Your action was successful!')

    else:
      form = CustomUserCreationForm()
    return render(request ,'register_usercreationform_inheriting.html' , {'form':form})

           
# login using AuthenticationForm 
def loginAuthenticationForm(request):
    if request.method == 'POST':   # 1.If the user is submitting the login form
    
        fm = AuthenticationForm (request=request, data =request.POST) # 2.Process the form data

           #################################
           
        if fm.is_valid():    # 3.Check if the form is valid
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
        #################################
             
            user = authenticate(username=uname,password=upass) #checks that username and password against the database. 
                                        # - If a user with the given credentials exists and is active, it returns the user object.
            
            if user is not None: # If the user exists and credentials are correct
                login(request , user)  # Log the user in
                return HttpResponseRedirect('/myapp/contact/')
       
            else:
                messages.error(request, "Invalid username or password.")  # Error message for wrong credentials
            #################################
        else:
            messages.error(request, "Invalid form data. Please check your input.")  # Form validation error
            return render(request, 'login-AuthenticationForm.html', {'form': fm})
        #####################################
        
     # If we reach this point, it means login failed. Re-render the form with error messages.  
     # If the request method is not POST (e.g., GET), render the login form  
    else:
        fm = AuthenticationForm()
        return render (request , 'login-AuthenticationForm.html',{'form':fm})
        
        
        
