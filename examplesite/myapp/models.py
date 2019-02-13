from django.db import models
import uuid

# Create your models here.



class SchoolsModel(models.Model):
    school_name = models.CharField(max_length=100)
    num_max_students = models.IntegerField()
    
    
    def __str__(self):
        return self.school_name
    

class StudentsModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_identification_string  = models.AutoField(primary_key=True)
    school = models.ForeignKey(SchoolsModel, on_delete=models.CASCADE)
