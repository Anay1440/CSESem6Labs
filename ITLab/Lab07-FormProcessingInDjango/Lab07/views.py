from django.shortcuts import render, HttpResponse
from .forms import Q1Form, Q2Form

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Q1FormPage(request):
    context = {}
    form = Q1Form(request.POST)
    context['form'] = form
    return render(request, 'Q1FormPage.html', context)

def Q1FormSubmit(request):
    car_manufacturer = "N/A"
    model_name = "N/A"

    if request.method == "POST":
        # Get the posted form
        MyForm = Q1Form(request.POST)
    if MyForm.is_valid():
        car_manufacturer = MyForm.cleaned_data['car_manufacturer']
        model_name = MyForm.cleaned_data['model_name']
    else:
        MyForm = Q1Form()

    context = {'car_manufacturer': car_manufacturer, 'model_name': model_name}

    return render(request, 'Q1ResultPage.html', context)

def Q2FormSubmit(request):
    context = {}
    if request.method == "POST":
        # Get the posted form
        MyForm = Q2Form(request.POST)
    if MyForm.is_valid():
        name = MyForm.cleaned_data['name']
        rno = MyForm.cleaned_data['rno']
        subject = MyForm.cleaned_data['subject_select']
        request.session['name'] = name
        request.session['rno'] = rno
        request.session['subject'] = subject
        context['name'] = name
        context['rno'] = rno
        context['subject'] = subject 
    else:
        MyForm = Q2Form()

    return render(request, 'Q2ResultPage.html', context)

def Q2FirstPage(request):
    if request.session.has_key('name'):
        context = {}
        context['name'] = request.session['name']
        context['rno'] = request.session['rno']
        context['subject'] = request.session['subject']
        return render(request, 'Q2ResultPage.html', context)
    else:
        return render(request, 'Q2FormPage.html')
    
def Q2Reset(request):
    try:
        del request.session['name']
        del request.session['rno']
        del request.session['subject']
    except:
        pass
    return render(request, 'Q2FormPage.html')