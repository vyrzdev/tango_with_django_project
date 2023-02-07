from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)


def about(request: HttpRequest):
    context_dict = {'boldmessage': 'This tutorial has been put together by Ben.'}

    return render(request, 'rango/about.html', context=context_dict)
