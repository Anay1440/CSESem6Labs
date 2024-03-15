"""
Definition of urls for Lab08_Forms_Django_II.
"""

from django.urls import path
from Lab08 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Q1/', views.Q1RegisterPage, name='Q1'),
    path('Q1ResultPage/', views.Q1FormSubmit, name='Q1FormSubmit'),
    path('Q2', views.Q2FirstPage, name='Q2'),
    path('Q2ResultPage', views.Q2FormSubmit, name='Q2FormSubmit'),
    path("Q2Reset", views.Q2Reset, name="Q2Reset"),
    path("Q3", views.Q3, name='Q3'),
    path("Q3Voted", views.Q3FormSubmit, name='Q3FormSubmit'),
]
