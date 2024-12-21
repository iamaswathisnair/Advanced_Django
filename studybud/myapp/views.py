from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime , date 
from .forms import ContactForm , Ordering_form_fields_form ,Userform
from .form_widgets import DemowidgetForm
from .modelform_inheritance import EmployeeForm ,Teacherform
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def learn_django(request):
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
         print("success")
    else:
        formm = UserCreationForm()
    return render(request ,'user_reg.html' , {'fm':formm})
