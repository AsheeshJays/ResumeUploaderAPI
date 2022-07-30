from django.urls import path 
from mainApp.api import views

urlpatterns = [
    path('resume/',views.ResumeView.as_view(),name='resume'),
    path('list/',views.ResumeView.as_view(),name='list'),
]
