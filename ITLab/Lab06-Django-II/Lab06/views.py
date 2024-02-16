from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Q1(request):
    return render(request, 'Q1.html')

def Q2(request):
    return render(request, 'Q2.html')

def Q3Home(request):
    return render(request, 'Q3Home.html')

def Q3RedirectToHome(request):
    return redirect('/Q3/Home')

def Q3Metadata(request):
    return render(request, 'Q3Metadata.html')

def Q3Reviews(request):
    return render(request, 'Q3Reviews.html')

def Q3PublisherInfo(request):
    return render(request, 'Q3PublisherInfo.html')
