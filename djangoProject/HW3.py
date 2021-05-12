# create proj directory
django-admin startproject proj

# Change working directory to the django directory
cd C:\Users\mac\Box Sync\UC Davis\Courses\djangoProject\proj

# verity that the django project works
python manage.py runserver

# visited http://127.0.0.1:8000/ and got the congratulations message. Next step is to create the app.
# very important note: polls needs to be nested within proj! Otherwise the server would not run.
python manage.py startapp polls

# the following codes pasted into polls/views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# urls.py file added into polls and the following codes pasted in urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# pasted the following into proj\urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('proj.polls.urls')),
    path('admin/', admin.site.urls),
]

# verify to see if it worked.
python manage.py runserver

# visited http://localhost:8000/polls/ and got the right message. Hooray!

# go to proj/settings.py, set the time zone to America/Los_Angeles, and create the tables in the database
python manage.py migrate

# stopped before the creating models section

# Based on what you learned in Part 1, create a new view that welcomes a user to your website and tells them the
# current time. This is the view they will see if they navigate to your website, which, if it is running on your
# development server has the URL: http://127.0.0.1:8000/ (Links to an external site.)or equivalently
# http://localhost:8000/ (Links to an external site.).

# create view directory
cd C:\Users\mac\Box Sync\UC Davis\Courses\djangoProject\
django-admin startproject view

# Change working directory to the django directory
cd C:\Users\mac\Box Sync\UC Davis\Courses\djangoProject\view

# verity that the django project works
python manage.py runserver

# visited http://127.0.0.1:8000/ and got the congratulations message. Next step is to create the app.
# very important note: welcome needs to be nested within view! Otherwise the server would not run.
python manage.py startapp welcome

# the following codes pasted into welcome/views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi there! Welcome to my website!")

# urls.py file added into welcome and the following codes pasted in urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# pasted the following into view\urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('welcome/', include('welcome.urls')),
    path('admin/', admin.site.urls),
]

# get current time depending on the timezone
import datetime

now = datetime.datetime.now().strftime('%H:%M:%S')  #  Time formatted like '23:12:05'

# verify to see if it worked.
python manage.py runserver

# visited http://localhost:8000/welcome/ and got the right message. Hooray!
firstnames = ['Zeno', 'Rice']
lastnames = ['Kramer', 'Kramer']
dobs = ['2017-03-17', '2018-04-18']
ages = [4, 3]
genders = ['F','F']
   for lastname in lastnames:
        person, created = Person.objects.get_or_create(lastname=lastname)
        if created:
            print(f"Created an entry for {lastname}")
    for dob in dobs:
        person, created = Person.objects.get_or_create(dob=dob)
        if created:
            print(f"Created an entry for {dob}")
    for age in ages:
        person, created = Person.objects.get_or_create(age=age)
        if created:
            print(f"Created an entry for {age}")
    for gender in genders:
        person, created = Person.objects.get_or_create(gender=gender)
        if created:
            print(f'Created an entry for {gender}')