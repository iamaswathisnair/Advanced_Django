"""
URL configuration for studybud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.conf import settings
# from django.conf.urls.static import static

from django.urls import path
from . import views
                    # from .views import set_password_view, custom_set_password_view 

urlpatterns = [
    
 path('learn_django/',views.learn_django,name='learn_django'),
 path('learn_tags/',views.learn_tags,name='learn_tags'),
 path('oper_tags/',views.oper_tags,name='oper_tags'),
 path('for_tags/',views.for_tags,name='for_tags'),
 path('for_static/',views.for_static,name='for_static'),
 path('temp_inheritance/',views.temp_inheritance,name='temp_inheritance'),
 path('about/',views.about,name='about'),
 path('contact/',views.contact,name='contactus'),
 path('for_urls/',views.for_urls,name='for_urls'),
 path('include_tag/',views.include_tag,name='include_tag'),
 path('contact_view/',views.contact_view,name='contact_view'),
 path('Ordering_form_fields_view/',views.Ordering_form_fields_view,name='Ordering_form_fields_view'),
 path('DemowidgetForm_view/',views.DemowidgetForm_view,name='DemowidgetForm_view'),
 path('usermodelform/',views.usermodelform,name='usermodelform'),
 path('emp_model_inheritence/',views.emp_model_inheritence,name='emp_model_inheritence'),
 path('teacher_model_inheritance/',views.teacher_model_inheritance,name='teacher_model_inheritance'),
 path('user_reg/',views.user_reg,name='user_reg'),
 path('register/',views.register,name='register'),
 path('loginAuthenticationForm/',views.loginAuthenticationForm,name='loginAuthenticationForm'),
 path('logout_view/',views.logout_view,name='logout'),
 path('change_password/',views.change_password,name='change_password'),
 path('set-password/', views.set_password, name='set_password'),
 
 
 
 
 path('type1/',views.type1,name='type1'),
 
 
 ]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)