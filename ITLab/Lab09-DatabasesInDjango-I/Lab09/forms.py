from django import forms

class Q2RetrieveForm(forms.Form):
    company_name = forms.CharField(label="Enter the name of the company", required=False, widget=forms.TextInput(attrs={'required': 'True'}))
