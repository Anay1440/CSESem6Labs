from django.shortcuts import render, redirect
from .forms import Q1Form, Q2Form, Q3Form

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Q1RegisterPage(request):
    context = {}
    form = Q1Form(request.POST)
    context['form'] = form
    return render(request, 'Q1RegisterPage.html', context)

def Q1FormSubmit(request):
    username, pwd, email_ID, contact_num = "N/A", "N/A", "N/A", "N/A"

    if request.method == "POST":
        # Get the posted form
        MyForm = Q1Form(request.POST)
    if MyForm.is_valid():
        username = MyForm.cleaned_data['username']
        pwd = MyForm.cleaned_data['pwd']
        email_ID = MyForm.cleaned_data['email_ID']
        contact_num = MyForm.cleaned_data['contact_num']
    else:
        MyForm = Q1Form()

    context = {'username': username, 'pwd': pwd, 'email_ID': email_ID, 'contact_num': contact_num}

    return render(request, 'Q1ResultPage.html', context)

def Q2FirstPage(request):
    if request.session.has_key('name'):
        context = {}
        context['name'] = request.session['name']
        context['cgpa'] = request.session['cgpa']
        return render(request, 'Q2ResultPage.html', context)
    else:
        context = {}
        form = Q2Form(request.POST)
        context['form'] = form
        return render(request, 'Q2FormPage.html', context)
    
def Q2FormSubmit(request):
    context = {}
    if request.method == "POST":
        # Get the posted form
        MyForm = Q2Form(request.POST)
    if MyForm.is_valid():
        request.session['name'] = context['name'] = MyForm.cleaned_data['name']
        request.session['cgpa'] = context['cgpa'] = MyForm.cleaned_data['marks'] / 50
    else:
        MyForm = Q2Form()

    return render(request, 'Q2ResultPage.html', context)
    
def Q2Reset(request):
    try:
        del request.session['name']
        del request.session['cgpa']
    except:
        pass
    context = {}
    form = Q2Form(request.POST)
    context['form'] = form
    return render(request, 'Q2FormPage.html', context)

def Q3(request):
    context = {'votes': [0, 0, 0], 'voted': False}
    if 'votes' in request.session:
        context['votes'] = request.session['votes']
    return render(request, 'Q3.html', context)

def Q3FormSubmit(request):
    context = {'votes': [], 'voted': True}

    if request.method == "POST":
        MyForm = Q3Form(request.POST)
    if MyForm.is_valid():
        vote = int(MyForm.cleaned_data['vote']) - 1
        if 'votes' in request.session:
            request.session['votes'][vote] += 1
        else:
            request.session['votes'] = [0, 0, 0]
            request.session['votes'][vote] += 1

        request.session.modified = True
            
        total_votes = sum(request.session['votes'])
        context['votes'] = [round((i * 100 / total_votes), 3) for i in request.session['votes']]
    
    return render(request, 'Q3.html', context)

def Q3Reset(request):
    try:
        del request.session['votes']
    except:
        pass
    return redirect('Q3')
