from django.shortcuts import render
from myapp.models import SchoolsModel, StudentsModel
from rest_framework import viewsets
from myapp.serializers import StudentsSerializer, SchoolsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView,ListCreateAPIView


class StudentsListView(ListCreateAPIView):
    queryset = StudentsModel.objects.all()
    serializer_class = StudentsSerializer
    
class SchoolsListView(ListCreateAPIView):
    queryset = SchoolsModel.objects.all()
    serializer_class = SchoolsSerializer
    
class StudentDetailView(RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = StudentsModel.objects.all()
    serializer_class = StudentsSerializer
    
class SchoolDetailsView(RetrieveUpdateAPIView):
    queryset = SchoolsModel.objects.all()
    serializer_class = SchoolsSerializer
    