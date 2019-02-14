from rest_framework import serializers
from myapp.models import SchoolsModel, StudentsModel

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsModel
        fields = ('first_name', 'last_name','student_identification_string', 'school')


class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolsModel
        fields = ('school_name', 'num_max_students')

class StudentNestedViewSetSerializer(serializers.ModelSerializer):
        class Meta:
            model = StudentsModel
            fields = ('first_name', 'last_name','student_identification_string', 'school')