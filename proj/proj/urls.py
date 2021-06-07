"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from proj import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('people/add/', views.add_person, name='add_person'),
    path('instructions/', views.instructions, name='instructions'),
    path('practice1/add/', views.add_practice1, name='add_practice1'),
    path('practice2/add/', views.add_practice2, name='add_practice2'),
    path('practice3/add/', views.add_practice3, name='add_practice3'),
    path('practice4/add/', views.add_practice4, name='add_practice4'),
    path('observation1/add/', views.add_observation1, name='add_observation1'),
    path('observation2/add/', views.add_observation2, name='add_observation2'),
    path('observation3/add/', views.add_observation3, name='add_observation3'),
    path('observation4/add/', views.add_observation4, name='add_observation4'),
    path('result1/', views.result1, name='result1'),
    path('result2/', views.result2, name='result2'),
]
