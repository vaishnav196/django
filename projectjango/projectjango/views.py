from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def industry(request):
    return render(request,'industry.html')

def panel(request):
    return render(request,'panel.html')

def qual(request):
    return render(request,'qual.html')

def Quan(request):
    return render(request,'Quan.html')

def other(request):
    return render(request,'other.html')

def contact(request):
    return render(request,'contact.html')

def coverage(request):
    return render(request,'coverage.html')
