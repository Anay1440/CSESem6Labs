"""
Definition of urls for Lab09_Databases_Django_I.
"""

from django.urls import include, path
from django.contrib import admin

admin.autodiscover()
from Lab09_Solved import views as solved_views
from Lab09 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Q2', views.Q2, name='Q2'),
    path('Q2WorksForm', views.Q2RenderWorksFormPage, name='Q2WorksForm'),
    path('Q2LivesForm', views.Q2RenderLivesFormPage, name='Q2LivesForm'),
    path('Q2WorksFormSubmit', views.Q2WorksFormSubmit, name='Q2WorksFormSubmit'),
    path('Q2LivesFormSubmit', views.Q2LivesFormSubmit, name='Q2LivesFormSubmit'),
    path('Q2RetrieveFormSubmit', views.Q2RetrieveFormSubmit, name='Q2RetrieveFormSubmit'),

    # Solved Views:
    path('Solved/', solved_views.archive, name='Archive'),
    path('Solved/blog/', include('Lab09_Solved.urls')),
    path('Solved/admin', admin.site.urls),
]
