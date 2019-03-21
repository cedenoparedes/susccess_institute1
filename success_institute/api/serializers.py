from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Student, Group, student_group


class StudentSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Student
        fields = ('id', 'user_id', 'career')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name')


class GroupStudentSerializer(serializers.ModelSerializer):

    student = serializers.IntegerField(write_only=True)
    group_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = student_group
        fields = ('id', 'student', 'group_id', )








