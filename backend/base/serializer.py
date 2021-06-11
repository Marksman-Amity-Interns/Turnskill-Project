from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import skill_course

class skill_courseSerailizer(serializers.ModelSerializer):
    class Meta:
        model = skill_course
        fields = '__all__'
