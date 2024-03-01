from django import forms

class Solved_RegForm(forms.Form): 
    title = forms.CharField() 
    description = forms.CharField() 
    views = forms.IntegerField() 
    available = forms.BooleanField()

class Solved_LoginForm(forms.Form):
    username = forms.CharField(max_length= 100)
    contact_num = forms.IntegerField()

class Solved_Session_LoginForm(forms.Form):
    username = forms.CharField(max_length= 100)
    password = forms.CharField(widget=forms.PasswordInput())