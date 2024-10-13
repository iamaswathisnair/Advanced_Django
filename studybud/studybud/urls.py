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
# include('myapp.urls'): This tells Django to look in myapp/urls.py for further URL patterns when a URL starts with myapp/.
# The 'myapp/' part is a prefix. If you access http://localhost:8000/myapp/learn/, it will load the learn_django view from myapp/urls.py.
from django.contrib import admin
from django.urls import path , include
  
#  make sure you are including the URLs from your app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')), # include the app's urls
    # path('coursee/', include('course(app_name).urls')),
    
]
