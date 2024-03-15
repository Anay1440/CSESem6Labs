from django import forms

class Q1Form(forms.Form):
    username = forms.CharField(label="Enter username", required=False, widget=forms.TextInput(attrs={'required': 'True'}))
    pwd = forms.CharField(label="Enter password", required=False, widget=forms.PasswordInput)
    email_ID = forms.CharField(label="Enter email ID", required=False, widget=forms.EmailInput)
    contact_num = forms.IntegerField(label="Enter contact number", required=False, widget=forms.NumberInput)


class Q2Form(forms.Form):
    name = forms.CharField(max_length= 100, required=False, widget=forms.TextInput(attrs={'required': 'True'}))
    marks = forms.IntegerField(label="Enter total marks", required=False, widget=forms.NumberInput(attrs={'required': 'True'}))
    

class Q3Form(forms.Form):
    choices = ((1, 'Good'), (2, 'Satisfactory'), (3, 'Bad'))
    vote = forms.ChoiceField(label="How is the book ASP.NET with C# by Vipul Prakashan?", required=False, 
                             widget=forms.RadioSelect(attrs={'required': 'True'}), choices=choices)