from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def calculate(x, y):
    return x + y


def hello(request, color):
    x = calculate(1, 3)
    return HttpResponseRedirect(reverse("color-url", args=[color]))


def color(request, color):
    return render(request, 'color.html', {'color': color})
