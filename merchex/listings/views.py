import http
from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Band
# Create your views here.


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
    <h1>Hello Django !</h1>'
    <p>My favorite bands are:<p>
    <ul>
     <li>{bands[0].name}</li>
     <li>{bands[1].name}</li>
     <li>{bands[2].name}</li>
    </ul>
    """)


def about(request):
    return HttpResponse('<h1>About us </h1> <p>we love merch !</p>')


def listings(request):
    return HttpResponse('<h1>This is my listing page </h1> <p>later on we will show you the list of service we offer in this website !</p>')


def contacts(request):
    return HttpResponse('<h1>This is the contact page </h1> <p> her you can find our contact details !</p>')
