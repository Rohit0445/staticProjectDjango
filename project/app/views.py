from django.shortcuts import render

# Create your views here.
def landingpage(req):
    return render(req,'landing.html')
