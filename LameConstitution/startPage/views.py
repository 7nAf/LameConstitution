from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    try:
        return render(request, "home.html") 
    except NameError:
        return HttpResponse("Hello, world. You're at the polls index.")
