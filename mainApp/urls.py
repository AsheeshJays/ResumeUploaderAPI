from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('candidate/<int:pk>/', views.CandidateView.as_view(),name='candidate')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
