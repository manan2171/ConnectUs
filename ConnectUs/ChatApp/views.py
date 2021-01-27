from django.shortcuts import render
from django.http import *
# Create your views here.
def hello(requst):
    return HttpResponse("hello world")