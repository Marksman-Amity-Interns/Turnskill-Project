from rest_framework import serializers
from django.http.response import HttpResponse
from .models import course, user
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializer import CourseSerializer, UserForCourseSerializer


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/users/',
        '/api/user/<id>',
        
        '/api/courses/',
        '/api/course/<id>',
    ]
    
    return Response(routes)

@api_view(['GET'])
def getCourses(request):
    courses = course.objects.all()
    courses_data = CourseSerializer(courses, many = True)
    print(courses)
    return Response(courses_data.data)


@api_view(['GET'])
def getCourse(request,pk):
    course_obj = course.objects.filter(course_id = pk)
    user_obj = course_obj[0].instructor
    user_data = UserForCourseSerializer(user_obj)
    courses_data = CourseSerializer(course_obj[0], many = False)
    # print(course_obj)
    # print(user_data.data)
    return Response({'courses_details':courses_data.data, 'user_details':user_data.data})

    