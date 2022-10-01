from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobbies


# Create your views here.
def home(request):
    return HttpResponse("Hello and welcome to my site. My name is Cory Coleman. I am a senior in the "
                        "Computer Science Program at Weber State University. "
                        "I am working on finishing up my Bachelor's Degree in "
                        "Web and User experience. I am creating this site through my "
                        "CS 3620 - Server-side Web Architecture course at Weber State University. " 
                        "I really love working with web development on the front-end side, "
                        "and I am very excited to be learning more about the back-end side.")


def hobbies(request):
    hobby_list = Hobbies.objects.all()
    return HttpResponse(hobby_list)


def portfolio(request):
    p_list = Portfolio.objects.all()
    return HttpResponse(p_list)


def contact(request):
    return HttpResponse("Email: corycoleman@mail.weber.edu")
