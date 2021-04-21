from django.shortcuts import render

# Create your views here.
import datetime

now = datetime.datetime.now().strftime('%H:%M:%S')

from django.http import HttpResponse


def index(request):
    return HttpResponse(f'Hi there! Welcome to my website! The current time is {now}.')