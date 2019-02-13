from django.shortcuts import render
from myapp.models import SchoolsModel, StudentsModel
from rest_framework import viewsets
from myapp.serializers import StudentsSerializer, SchoolsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from django.shortcuts import get_object_or_404, render


class StudentsListView(ListCreateAPIView):
    queryset = StudentsModel.objects.all()
    serializer_class = StudentsSerializer


        
        
class SchoolsListView(ListCreateAPIView):
    queryset = SchoolsModel.objects.all()
    serializer_class = SchoolsSerializer
    
class StudentDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete.
    """
    queryset = StudentsModel.objects.all()
    serializer_class = StudentsSerializer
    
class SchoolDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = SchoolsModel.objects.all()
    serializer_class = SchoolsSerializer
    