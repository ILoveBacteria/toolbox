from django.urls import path

from website import views


urlpatterns = [
    path('api/certificate', views.CertificateList.as_view()),
    path('api/education', views.EducationList.as_view()),
    path('api/experience', views.ExperienceList.as_view()),
    path('api/ping', views.ping),
]
