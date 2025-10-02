from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    #normal response
    stuinfo=["name","geetik","age",21,"dob",181104]
    return HttpResponse( stuinfo )
