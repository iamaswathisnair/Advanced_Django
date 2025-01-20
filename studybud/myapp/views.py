# onn vere temlate same fileds as in usercraetinform , 2 kore filedsss vechitt 
from django.shortcuts import render , HttpResponseRedirect , redirect
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
from django.contrib.auth.forms import PasswordChangeForm ,  SetPasswordForm # Import the form
from django.contrib.auth import update_session_auth_hash  # Keep the user logged in after password change


# {% url 'view_name' %}
#msge kazhinj ethilky aano render eethe ah pagil aan msge dispslay aava


# Create your views here.

def learn_django(request):  #request: Represents the HTTP request sent by the client (e.g., a browser).
    d=datetime.now()  #datetime.now() for the full date and time.
    d1=date.today() # from the datetime module for just the current date.
    return render (request , 'index.html' , {'name':"achu","da":d,"da2":d1} ) 
    
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
    


"""----------------------------------------------------"""



#reg using django built-in usercreationform

def user_reg(request):
    if request.method == 'POST':  # Check if the request method is POST, which indicates that the form has been submitted.
     formm =UserCreationForm(request.POST) #Passing request.POST to the form tells Django: --- "Hey, here's the data the user submitted. Please check if it's valid."
     if formm.is_valid():
         user = formm.save()
         
         request.session['username'] = user.username   # for getting name after wlcome or smthing nbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
         return render(request, 'about.html', {'username': user.username})
     
     
    else:
        formm = UserCreationForm()
    return render(request ,'user_reg.html' , {'fm':formm})

        # try:
        #     user = User.objects.create_user(username=username, password=password1)
        #     user.save()
        #     messages.success(request, "Registration successful! You can now log in.")
        #     return redirect('login')  # Redirect to login after successful registration
        # except Exception as e:
        #     messages.error(request, f"Error: {e}")
        #     return redirect('register')  # Return to register page if something goes wrong
        
        
        
        
#inheriting UserCreation form to add more fields 

def register(request):
    if request.method == 'POST':
       form = CustomUserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, 'Your action was successful!')
           return render (request , 'login-AuthenticationForm.html')

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
                # return HttpResponseRedirect('/myapp/learn_django/' , {'username': uname})
                context = {
                    'username': uname,
                    'da': datetime.now(),
                    'da2': datetime.now().date(),
        }
                return render (request , 'index.html' , context)
            
                        #redirect() is more flexible because it can take either a URL string, view name, or even model. return redirect('contact')
                        #You could say, “Take the user to a page called 'contact'” (instead of typing /myapp/contact/ directly).    
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
        

#LOGOUT 
def logout_view(request):
    logout(request)    # This clears the session and logs the user out  
    messages.success(request , "logout suceesfullyy brooo")
    fm = AuthenticationForm()
    return redirect ('loginAuthenticationForm')  
     


# change password knowing old password  PasswordChangeForm
def change_password(request):
    if request.user.is_authenticated:   #nbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        if request.method =='POST':
            fm = PasswordChangeForm( request.user , request.POST)
            # fm = PasswordChangeForm(user =request.user , data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, request.user)  # Prevent the user from being logged out
                return redirect('learn_django')
        else:
            fm = PasswordChangeForm(request.user)
            return render(request , 'change_password.html', {'form':fm})
        
    else:
        return redirect('loginAuthenticationForm')
        
# change password without knowing old password  SetPasswordForm

def set_password(request):
    if request.method =='POST':
        fm = SetPasswordForm(request.user ,request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, request.user)  # Prevent the user from being logged out
            return redirect('learn_django')
        else:
            # FOR Handle invalid form
            #fm =SetPasswordForm(request.user) # Do NOT reinitialize the form, render it with errors so this fm not require
            return render(request, 'set_pass.html', {'form': fm})
    else:
        fm =SetPasswordForm(request.user)
        return render(request , 'set_pass.html', {'form':fm})
            
            
    
    
        
def type1(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully!")
            return redirect('learn_django')  # Redirect to home or login page
        else:
            # Debugging: Print form errors in the console
            print("Form Errors:", form.errors)
            messages.error(request, "achuuu Form submission failed. Please correct the errors.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'type1reg.html', {'form': form})
