from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import course, user

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'count_course', 'job', 'email']

class UserForCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['email']
