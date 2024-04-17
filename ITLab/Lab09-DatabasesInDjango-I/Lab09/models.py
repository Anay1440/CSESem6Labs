from django.db import models
from django.forms import ModelForm

# Create your models here.

class Q2Works(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    salary = models.IntegerField()

class Q2WorksForm(ModelForm):
    class Meta:
        model = Q2Works
        fields = ['name', 'company_name', 'salary']

class Q2Lives(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Q2LivesForm(ModelForm):
    class Meta:
        model = Q2Lives
        fields = ['name', 'street', 'city']