from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/users/',
        '/api/user/<id>',
        
        '/api/courses/',
        '/api/course/<id>',

        '/api/virtual-classrooms/',
        '/api/virtual-classroom/<id>',

        '/api/mentors/',
        '/api/mentor/<id>',
    ]
    return Response(routes)
