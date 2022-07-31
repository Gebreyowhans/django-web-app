import http
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse('<h1>Hello Django ! </>')


def about(request):
    return HttpResponse('<h1>About us </h1> <p>we love merch !</p>')


def listings(request):
    return HttpResponse('<h1>This is my listing page </h1> <p>later on we will show you the list of service we offer in this website !</p>')


def contacts(request):
    return HttpResponse('<h1>This is the contact page </h1> <p> her you can find our contact details !</p>')
