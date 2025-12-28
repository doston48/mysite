from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage (request) :
  return HttpResponse("<h1>This is homepage! Welcome to Django!</h1>")

def about (request):
  return HttpResponse("<hl>This is about page!</h1>")