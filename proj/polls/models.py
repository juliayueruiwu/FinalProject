import datetime
from django.db import models


# Create your models here.
# create person variables
class Person(models.Model):
    FirstName = models.CharField(blank=False, max_length=60)
    LastName = models.CharField(blank=False, max_length=60)
    DOB = models.DateField(auto_now_add=False, null=True)
    Age = models.IntegerField(null=True)
    gender_options = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    Gender = models.CharField(choices=gender_options, null=True, default=False, max_length=60)

    # add this to avoid returning person object 1 and 2 in websites
    def __str__(self):
        return self.FirstName

# create behavior variables
class Behavior(models.Model):
    trial1_options = [
        ('R', 'Red'),
        ('B', 'Blue')
    ]
    trial2_options = [
        ('R', 'Red'),
        ('B', 'Blue')
    ]
    trial3_options = [
        ('R', 'Red'),
        ('B', 'Blue')
    ]
    trial4_options = [
        ('R', 'Red'),
        ('B', 'Blue')
    ]
    trial5_options = [
        ('R', 'Red'),
        ('B', 'Blue')
    ]
    trial6_options = [
        ('R', 'Red'),
        ('B', 'Blue')
    ]
    trial7_options = [
        ('R', 'Red'),
        ('B', 'Blue')
    ]
    trial8_options = [
        ('R', 'Red'),
        ('B', 'Blue')
    ]
    trial9_options = [
        ('R', 'Red'),
        ('B', 'Blue')
    ]
    trial10_options = [
        ('R', 'Red'),
        ('B', 'Blue')
    ]
    trial1 = models.CharField(choices=trial1_options, null=True, default=False, max_length=60)
    trial2 = models.CharField(choices=trial2_options, null=True, default=False, max_length=60)
    trial3 = models.CharField(choices=trial3_options, null=True, default=False, max_length=60)
    trial4 = models.CharField(choices=trial4_options, null=True, default=False, max_length=60)
    trial5 = models.CharField(choices=trial5_options, null=True, default=False, max_length=60)
    trial6 = models.CharField(choices=trial6_options, null=True, default=False, max_length=60)
    trial7 = models.CharField(choices=trial7_options, null=True, default=False, max_length=60)
    trial8 = models.CharField(choices=trial8_options, null=True, default=False, max_length=60)
    trial9 = models.CharField(choices=trial9_options, null=True, default=False, max_length=60)
    trial10 = models.CharField(choices=trial10_options, null=True, default=False, max_length=60)

    def __str__(self):
        return self.trial1

# create observation variables indexing person and behavior, plus a time stamp
# for some reason, got the error "TypeError: __init__() got an unexpected keyword argument 'auto_now_add'"
# when "auto_now_add=False" was added to the dob variable
class Observation(models.Model):
    player1 = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='player2')
    behavior = models.ForeignKey('Behavior', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


# run py manage.py makemigrations polls and then py manage.py sqlmigrate polls 0002 and py manage.py migrate
# something seems wrong?? I cannot open the website and it says"...Running migrations:
#   No migrations to apply." Not sure if this is because I did not make any changes to the migration.