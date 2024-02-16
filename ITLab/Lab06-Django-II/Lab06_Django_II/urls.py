"""
Definition of urls for Lab06_Django_II.
"""

from django.urls import path
from Lab06 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Q1/', views.Q1, name='Q1'),
    path('Q2/', views.Q2, name='Q2'),
    path('Q3/', views.Q3RedirectToHome, name='Q3'),
    path('Q3/Home', views.Q3Home, name='Q3Home'),
    path('Q3/Metadata', views.Q3Metadata, name='Q3Metadata'),
    path('Q3/Reviews', views.Q3Reviews, name='Q3Reviews'),
    path('Q3/PublisherInfo', views.Q3PublisherInfo, name='Q3PublisherInfo'),
]
