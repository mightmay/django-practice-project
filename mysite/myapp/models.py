from django.db import models

# Create your models here.



class Schools(models.Model):
    school_name = models.CharField(max_length=100)
    num_max_students = models.IntegerField()
    

class Students(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
