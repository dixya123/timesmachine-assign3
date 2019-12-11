from django.shortcuts import render
from django.http import HttpResponse
import time
import datetime

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello how are you!!</h1>')

def today(request):
    return HttpResponse("Todays date is:{}".format(datetime.date.today()))


def timestamp(request):
    return HttpResponse("Timestamp is :{}".format(time.time()))

