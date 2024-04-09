from rest_framework import serializers
from mother.models import Mother,Child
from teacher.models import Teacher,Report

class MotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mother
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

# class NoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Child
#         fields = ['notes']