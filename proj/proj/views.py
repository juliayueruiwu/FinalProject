# proj views

from django.shortcuts import render

from polls.models import Person

from proj.forms import PersonForm, ObservationForm

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import pdb

def index(request):
    template = 'proj/base.html'

    return render(request, template, {})

def message(request,msg=''):
    template = 'proj/message.html'
    return render(request,template,{'message':msg})

def list_people(request):
    template = 'proj/list_people.html'
    people = Person.objects.all()

    # create our context dictionary
    context = {
        'people': people,
    }

    return render(request, 'proj/list_people.html', context)

def add_person(request):
    template = 'proj/add_person.html'

    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            form.save()

            new_user = form.cleaned_data['firstname']
            message = f'Created new user: {new_user}'

            return HttpResponseRedirect(reverse('message',kwargs={'msg':message}))
    else:
        form = PersonForm()

    context={
        'form': form,
    }

    return render(request, template, context)

def list_observations(request):
    pass

def add_observation(request):
    template = 'proj/add_observation.html'

    if request.method == 'POST':
        form = ObservationForm(request.POST)

        if form.is_valid():
            form.save()

            message = f'Created new observation'

            # return render(request, 'proj/message.html', {'message': message})
            return HttpResponseRedirect(reverse('message', kwargs={'msg': message}))
    else:
        form = ObservationForm()

    context={
        'form': form,
    }

    return render(request, template, context)