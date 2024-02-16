from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Q1(request):
    return render(request, 'Q1.html')

def Q2(request):
    return render(request, 'Q2.html')