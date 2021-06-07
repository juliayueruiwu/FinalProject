# proj views

from django.shortcuts import render

from proj.models import Person, Practice, Round

from proj.forms import PersonForm, Observation1Form, Observation2Form, Observation3Form, Observation4Form, Practice1Form, Practice2Form, Practice3Form, Practice4Form

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

import pdb

def index(request):
    template = 'proj/base.html'

    return render(request, template, {})


# add instruction view
def instructions(request):
    template = 'proj/instructions.html'

    return render(request, template, {})

# add result 1 view that gives feedback on how many coins were earned after each round
def result1(request):
    template = 'proj/result1.html'

    return render(request, template, {})

# add result 1 view that gives feedback on how many coins were earned after each round
def result2(request):
    template = 'proj/result2.html'

    return render(request, template, {})

# add person view
def add_person(request):
    template = 'proj/add_person.html'

    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            form.save()

            new_user = form.cleaned_data['FirstName']
            message = f'Created new user: {new_user}'

            return HttpResponseRedirect(reverse('message',kwargs={'msg':message}))
    else:
        form = PersonForm()

    context={
        'form': form,
    }

    return render(request, template, context)

# add practice 1 view: if a choice is selected, return "Answer was recorded" message
def add_practice1(request):
    template = 'proj/add_practice1.html'

    if request.method == 'POST':
        form = Practice1Form(request.POST)

        if form.is_valid():
            form.save()

            message = f'Answer was recorded'

    else:
        form = Practice1Form()

    context={
        'form': form,
    }

    return render(request, template, context)

# add practice 2 view: if a choice is selected, return "Answer was recorded" message
def add_practice2(request):
    template = 'proj/add_practice2.html'

    if request.method == 'POST':
        form = Practice2Form(request.POST)

        if form.is_valid():
            form.save()

            message = f'Answer was recorded'

    else:
        form = Practice2Form()

    context={
        'form': form,
    }

    return render(request, template, context)

# add practice 3 view: if a choice is selected, return "Answer was recorded" message
def add_practice3(request):
    template = 'proj/add_practice3.html'

    if request.method == 'POST':
        form = Practice3Form(request.POST)

        if form.is_valid():
            form.save()

            message = f'Answer was recorded'

    else:
        form = Practice3Form()

    context={
        'form': form,
    }

# add practice 4 view: if a choice is selected, return "Answer was recorded" message
def add_practice4(request):
    template = 'proj/add_practice4.html'

    if request.method == 'POST':
        form = Practice4Form(request.POST)

        if form.is_valid():
            form.save()

            message = f'Answer was recorded'
    else:
        form = Practice4Form()

    context={
        'form': form,
    }

    return render(request, template, context)

# add game round 1 view: The other person [the computer] will always choose blue; redirect to different result views
# given different choices made by the participant
def add_observation1(request):
    template = 'proj/add_observation1.html'

    if request.method == 'POST':
        form = Observation1Form(request.POST)

        if form.is_valid():
            form.save()
            if form.cleaned_data['choice'] == 'R':
                return redirect('result1')
            if form.cleaned_data['choice'] == 'B':
                return redirect('result2')
    else:
        form = Observation1Form()

    context={
        'form': form,
    }

    return render(request, template, context)

# add game round 2 view: The other person [the computer] will always choose blue; redirect to different result views
# given different choices made by the participant
def add_observation2(request):
    template = 'proj/add_observation2.html'

    if request.method == 'POST':
        form = Observation2Form(request.POST)

        if form.is_valid():
            form.save()
            if form.cleaned_data['choice'] == 'R':
                return redirect('result1')
            if form.cleaned_data['choice'] == 'B':
                return redirect('result2')
    else:
        form = Observation2Form()

    context={
        'form': form,
    }

    return render(request, template, context)

# add game round 3 view: The other person [the computer] will always choose blue; redirect to different result views
# given different choices made by the participant
def add_observation3(request):
    template = 'proj/add_observation3.html'

    if request.method == 'POST':
        form = Observation3Form(request.POST)

        if form.is_valid():
            form.save()
            if form.cleaned_data['choice'] == 'R':
                return redirect('result1')
            if form.cleaned_data['choice'] == 'B':
                return redirect('result2')
    else:
        form = Observation3Form()

    context={
        'form': form,
    }

    return render(request, template, context)

# add game round 4 view: The other person [the computer] will always choose blue; redirect to different result views
# given different choices made by the participant
def add_observation4(request):
    template = 'proj/add_observation4.html'

    if request.method == 'POST':
        form = Observation4Form(request.POST)

        if form.is_valid():
            form.save()
            if form.cleaned_data['choice'] == 'R':
                return redirect('result1')
            if form.cleaned_data['choice'] == 'B':
                return redirect('result2')
    else:
        form = Observation4Form()

    context={
        'form': form,
    }

    return render(request, template, context)
