import datetime
from django.db import models


# create person variables to indicate user information
class Person(models.Model):
    FirstName = models.CharField(blank=False, max_length=60)
    LastName = models.CharField(blank=False, max_length=60)
    DOB = models.DateField(auto_now_add=False, null=True)
    Age = models.IntegerField(null=True)
    gender_options = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    Gender = models.CharField(choices=gender_options, null=False, max_length=60)

    # add this to avoid returning person object 1 and 2 in websites
    def __str__(self):
        return self.FirstName

# create practice variables to record responses in practice trials.
class Practice(models.Model):
    Practice_options = [
        (1, 'I will earn 0 coins; and the other person will earn 0 coins'),
        (2, 'I will earn 0 coins; and the other person will earn 2 coins'),
        (3, 'I will earn 2 coins; and the other person will earn 0 coins'),
        (4, 'I will earn 1 coin; and the other person will earn 1 coin')
    ]

    answer = models.IntegerField(choices=Practice_options, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

# create round variables to record responses in game trials.
class Round(models.Model):
    Round_options = [
        ('R', 'Red'),
        ('B', 'Blue')
    ]

    choice = models.CharField(choices=Round_options, null=False, max_length=60)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(default='', blank=True)

# run py manage.py makemigrations proj and then py manage.py sqlmigrate proj 0001_initial and py manage.py migrate