from django.shortcuts import render, HttpResponse
from .forms import Solved_RegForm, Solved_LoginForm, Solved_Session_LoginForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def solved(request):
    context = {}
    form = Solved_RegForm(request.POST or None)
    context['form'] = form
    return render(request, 'solved.html', context)

def solved_login(request):
    username = "not logged in"
    cn = "not found"
    if request.method == "POST":
        # Get the posted form
        MyLoginForm = Solved_LoginForm(request.POST)
    if MyLoginForm.is_valid():
        username = MyLoginForm.cleaned_data['username']
        cn = MyLoginForm.cleaned_data['contact_num']
    else:
        MyLoginForm = Solved_LoginForm()

    context = {'username': username, 'contact_num': cn}

    return render(request, 'solved_logged_in.html', context)

def solved_login_page(request):
    return render(request, 'solved_login_page.html')

def solved_session_login(request):
    username = "not logged in"
    if request.method == "POST":
        # Get the posted form
        MyLoginForm = Solved_Session_LoginForm(request.POST)
    if MyLoginForm.is_valid():
        username = MyLoginForm.cleaned_data['username']
        request.session['username'] = username
    else:
        MyLoginForm = Solved_Session_LoginForm()

    return render(request, 'solved_session_logged_in.html', {"username": username})

def solved_session_login_page(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'solved_session_logged_in.html', {"username": username})
    else:
        return render(request, 'solved_session_login_page.html')
    
def solved_session_logout(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponse("<strong>You are logged out</strong><br><a href='/Solved_Session_Login_Page'>Login</a>")