from django.urls import path
from . import views

urlpatterns = [
    path('api/education', views.EducationList.as_view()),
    path('api/experience', views.ExperienceList.as_view()),
    path('api/certificate', views.CertificateList.as_view()),
]
