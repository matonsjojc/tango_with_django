from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("heiii der pardnr. <a href='/rango/about/'>abut.</a>")

def about(request):
    return HttpResponse("abut. <a href='/rango/'>index.</a>")
