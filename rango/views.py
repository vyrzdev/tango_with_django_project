from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about'>About</a>")


def about(request: HttpRequest):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
