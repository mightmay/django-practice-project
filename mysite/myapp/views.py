from django.shortcuts import render
from myapp.models import Schools, Students
from rest_framework import viewsets
from myapp.serializers import StudentSerializer, SchoolSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows student to be viewed or edited.
    """
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows school to be viewed or edited.
    """
    queryset = Schools.objects.all()
    serializer_class = SchoolSerializer
# Create your views here.
