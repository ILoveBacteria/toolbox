from rest_framework import generics
from .serializers import *
from .models import *


class EducationList(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceList(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class CertificateList(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
