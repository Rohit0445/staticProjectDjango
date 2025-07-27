from django.shortcuts import render
from .models import Student


# Create your views here.
def landingpage(req):
    return render(req,'landing.html')



def register(req):
    return render(req,'register.html')


def login(req):
    return render(req,'login.html')


def ride(req):
    return render(req,'ride.html')



def drive(req):
    return render(req,'drive.html')