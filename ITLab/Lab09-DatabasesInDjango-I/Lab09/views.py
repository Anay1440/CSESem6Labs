from django.shortcuts import render, redirect
from .forms import Q2RetrieveForm
from Lab09.models import Q2Works, Q2Lives, Q2WorksForm, Q2LivesForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Q2WorksFormSubmit(request):
    if request.method == "POST":
        # Get the posted form
        form = Q2WorksForm(request.POST)
        if form.is_valid():
            works_entry = form.save(commit=False)
            works_entry.name = str(works_entry.name)
            works_entry.company_name = str(works_entry.company_name)
            works_entry.save()

    return redirect('/Q2')

def Q2LivesFormSubmit(request):
    if request.method == "POST":
        # Get the posted form
        form = Q2LivesForm(request.POST)
        if form.is_valid():
            lives_entry = form.save(commit=False)
            lives_entry.name = str(lives_entry.name)
            lives_entry.street = str(lives_entry.street)
            lives_entry.city = str(lives_entry.city)
            lives_entry.save()

    return redirect('/Q2')

def Q2(request):
    context = {'form': Q2RetrieveForm}
    return render(request, 'Q2.html', context)

def Q2RenderWorksFormPage(request):
    context = {'form': Q2WorksForm}
    return render(request, 'Q2WorksFormPage.html', context)

def Q2RenderLivesFormPage(request):
    context = {'form': Q2LivesForm}
    return render(request, 'Q2LivesFormPage.html', context)

def Q2RetrieveFormSubmit(request):
    if request.method == "POST":
        form = Q2RetrieveForm(request.POST)
    people = []
    if form.is_valid():
        company_name = form.cleaned_data['company_name']
        works_entries = Q2Works.objects.filter(company_name=company_name)
        people = []
        for item in works_entries:
            print(item.name)
            city_object = Q2Lives.objects.filter(name=item.name).first()
            if city_object:
                city = city_object.city
                people.append({'name': item.name, 'city': city})

    context = {'form': Q2RetrieveForm, 'people': people}
    print(context)
    return render(request, 'Q2.html', context)