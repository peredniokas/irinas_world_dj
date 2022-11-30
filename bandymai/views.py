from django.shortcuts import render
from django.http import HttpResponse


def pagrindinis(request):
    return render(request, 'triusis.html')