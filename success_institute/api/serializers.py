from django.contrib.auth.models import User
from rest_framework import serializers
from .models import student


class StudentSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = student
        fields = ('id', 'user_id', 'career')





