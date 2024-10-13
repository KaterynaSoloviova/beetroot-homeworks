from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.

def notes(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Notes app!")
