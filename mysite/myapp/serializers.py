from rest_framework import serializers
from myapp.models import Schools, Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('first_name', 'last_name','student_id', 'school')


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = ('school_name', 'num_max_students')

