from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def venki(request):
    return HttpResponse('<h2><marquee>i love u kata</marquee></h2>')