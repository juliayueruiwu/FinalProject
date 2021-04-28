# Within your app's directory, create a file called tasks.py that you can populate with various methods to assist
# your website, such as setting up initial values for models.
# (5 pts) Define a method that will populate the database table(s) for one or more of your models with some number of
# specific instances/entries Define a second method that performs each of the following

# run the python manage.py shell

from polls.models import Person, Behavior, Observation

import random
# firstnames of created users
def create_users():
    firstnames = ['Zeno', 'Rice']
    for firstname in firstnames:
        person, created = Person.objects.get_or_create(firstname=firstname)

        if created:
            print(f"Created an entry for {firstname}")

def create_behaviors():
    for behavior in Behavior.trial1_options:
        entry, created = Behavior.objects.get_or_create(trial1=behavior[0])

        if created:
            print(f"Created an entry for {behavior[1]}")

def create_observations():
    num_observations = 20

    people = Person.objects.all()
    behaviors = Behavior.objects.all()
    for iobs in range(0, num_observations):
        player1 = random.choice(people)
        possible_player2 = people.exclude(id=player1.id)
        player2 = random.choice(possible_player2)
        behavior = random.choice(behaviors)
        Observation.objects.create(player1=player1, player2=player2, behavior=behavior)
# from polls.tasks import create_users
# quit and reenter shell again, then run from polls.tasks import create_behaviors
# quit and reenter shell again, then run from polls.tasks import create_observations
# run from polls.models import Person, Behavior, Observation
Observation.objects.count()

# (2 pts) Retrieves and prints information about a specific object matching some criterion of your choosing.
# (3 pts) Retrieves and prints information for a subset (list) of entries that match a criterion of your choosing.
# list my player1
observations = Observation.objects.all()
observations.values_list('player1')
# list firstnames of my player1
observations.values_list('player1__firstname')
# Filter based on some criteria
observations.filter(player1__firstname='Rice')

