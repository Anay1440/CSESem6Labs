"""
Definition of urls for Lab07_Forms_Django.
"""

from django.urls import path
from Lab07_Solved import views as solved_views
from Lab07 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Q1/', views.Q1FormPage, name='Q1'),
    path('Q1ResultPage/', views.Q1FormSubmit, name='Q1FormSubmit'),
    path('Q2', views.Q2FirstPage, name='Q2'),
    path('Q2ResultPage', views.Q2FormSubmit, name='Q2FormSubmit'),
    path("Q2Reset", views.Q2Reset, name="Q2Reset"),

    # Solved Views:
    path('Solved/', solved_views.solved, name='Solved'),
    path('Solved_Login/', solved_views.solved_login, name='Solved_Login'),
    path('Solved_Login_Page/', solved_views.solved_login_page, name='Solved_Login_Page'),
    path('Solved_Session_Login', solved_views.solved_session_login, name="Solved_Session_Login"),
    path('Solved_Session_Login_Page', solved_views.solved_session_login_page, name="Solved_Session_Login_Page"),
    path("Solved_Session_Logout", solved_views.solved_session_logout, name="Solved_Session_Logout"),
]
