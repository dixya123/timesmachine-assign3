from django.contrib import admin
from django.urls import path
from timeteller.views import hello, today,timestamp

urlpatterns= [
    path('',hello),
    path('today/',today),
    path('timestamp/',timestamp)
]