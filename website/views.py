from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from website.models import Certificate, Education, Experience
from website.serializers import CertificateSerializer, EducationSerializer, ExperienceSerializer


@api_view(['GET'])
def ping(request):
    return Response({'ok': True})


class EducationList(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceList(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class CertificateList(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
