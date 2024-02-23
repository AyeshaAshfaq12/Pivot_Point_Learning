from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def personalized_learning(request):
    return render(request, 'personalized_learning.html')


def resources(request):
    return render(request, 'resources.html')


def contact(request):
    return render(request, 'contact.html')


def survey1(request):
    return render(request, 'survey1.html')


def survey2(request):
    return render(request, 'survey2.html')





