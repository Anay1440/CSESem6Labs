"""
Definition of urls for Lab05WebAppUsingDjango.
"""

from django.urls import path
from Lab05 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Q1/', views.Q1, name='Q1'),
    path('Q2/', views.Q2, name='Q2'),
]