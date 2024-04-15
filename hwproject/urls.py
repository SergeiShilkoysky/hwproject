"""
URL configuration for hwproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw1/', include('myhwapp.urls')),
    path('hw2/', include('myhwapp2.urls')),
    path('hw3/', include('myhwapp3.urls')),
    path('hw4/', include('myhwapp4.urls')),
    # path('hw5', include('myhwapp5.urls')),
    path('hw6', include('myhwapp6.urls')),
    # path('__debug__/', include("debug_toolbar.urls")),
]
