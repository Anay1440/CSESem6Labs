from django import forms

class Q1Form(forms.Form):
    choices = (('Audi', 'Audi'), ('Ferrari', 'Ferrari'), ('McLaren', 'McLaren'))
    car_manufacturer = forms.ChoiceField(label="Select a car manufacturer", required=False, widget=forms.Select(attrs={
        'required': 'True'
    }), choices=choices)
    model_name = forms.CharField(label="Enter the Model Name", required=False, widget= forms.TextInput(attrs={
                               'placeholder':'Model Name',
                               'required': 'True'
                            }))
    
class Q2Form(forms.Form):
    name = forms.CharField(max_length= 100)
    rno = forms.CharField(widget=forms.NumberInput())
    choices = (('Physics', 'Physics'), ('Chemistry', 'Chemistry'))
    subject_select = forms.ChoiceField(label="Select subject", required=False, widget=forms.Select(attrs={
        'required': 'True'
    }), choices=choices)