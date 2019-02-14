"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from myapp import views
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'schools', views.SchoolsListView)

domains_router = routers.NestedSimpleRouter(router, r'schools', lookup='schools')
domains_router.register(r'students', views.StudentNestedViewSet, base_name='schools-students')
# 'base_name' is optional. Needed only if the same viewset is registered more than once
 
urlpatterns = [
    path('students/', views.StudentsListView.as_view()),
    path('schools/', views.SchoolsListView.as_view()),
    path('schools/<int:pk>/', views.SchoolDetailsView.as_view()),
    path('students/<int:pk>/', views.StudentDetailView.as_view())
]




    
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += domains_router.urls