from django.shortcuts import render
from django.http import HttpResponse


def pagrindinis(request):
    return HttpResponse('Bandymu triusis')