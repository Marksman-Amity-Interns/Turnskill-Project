from django.http.response import HttpResponse
from .models import course, enrolment, user, video
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializer import CourseSerializer, UserForCourseSerializer, UserSerializer, UserSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user_data = UserSerializerWithToken(self.user).data
        for k,v in user_data.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/users/',
        '/api/users/<id>',
        
        '/api/courses/',
        '/api/courses/<id>',

        '/api/virtual-classroom/',
        '/api/virtual-classroom/<id>',

        '/api/mentor/',
        '/api/mentor/<id>',
    ]
    
    return Response(routes)

@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user_obj = user.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            job=data['job'],
            email = data['email'],
            password = make_password(data['password']),
        )
        serializer = UserSerializerWithToken(user_obj, many = False)
        return Response(serializer.data)
    except:
        message = {
            'detail' : 'User with this email already exists'
        }
        return Response(message, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = user.objects.all()
    users_data = UserSerializer(users, many = True)
    return Response(users_data.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user_obj = request.user
    user_details = UserSerializer(user_obj, many = False)
    course_ids = enrolment.objects.filter(user_id = user_obj.id)
    course_details = dict()
    for c in range(0, len(course_ids)):
        course_details[c] = course.objects.filter(title = course_ids[c].course_id).values()[0]
    return Response({ 'user_details': user_details.data,'courses_details':course_details})



@api_view(['GET'])
def getCourses(request):
    courses = course.objects.filter(islive=False)
    courses_data = CourseSerializer(courses, many = True)
    return Response(courses_data.data)


@api_view(['GET'])
def getCourse(request,pk):
    course_obj = course.objects.filter(course_id = pk, islive=False)
    instructor_obj = course_obj[0].instructor
    instructor_data = UserForCourseSerializer(instructor_obj)
    courses_data = CourseSerializer(course_obj[0], many = False)
    video_ids = video.objects.filter(course_id = pk)
    video_details = dict()
    for c in range(0, len(video_ids)):
        print(c)
        video_details[c] = video.objects.filter(video_id = video_ids[c].video_id).values()[0]
    return Response({'courses_details':courses_data.data, 'instructor_details':instructor_data.data , 'video_details': video_details})

@api_view(['GET'])
def getVirtualCourses(request):
    courses = course.objects.filter(islive=True, isonetoone=False)
    courses_data = CourseSerializer(courses, many = True)
    print(courses)
    return Response(courses_data.data)


@api_view(['GET'])
def getVirtualCourse(request,pk):
    course_obj = course.objects.filter(course_id = pk, islive=True, isonetoone=False)
    instructor_obj = course_obj[0].instructor
    instructor_data = UserForCourseSerializer(instructor_obj)
    courses_data = CourseSerializer(course_obj[0], many = False)
    video_ids = video.objects.filter(course_id = pk)
    video_details = dict()
    for c in range(0, len(video_ids)):
        print(c)
        video_details[c] = video.objects.filter(video_id = video_ids[c].video_id).values()[0]
    return Response({'courses_details':courses_data.data, 'instructor_details':instructor_data.data , 'video_details': video_details})

@api_view(['GET'])
def getMentorCourses(request):
    courses = course.objects.filter(islive=True, isonetoone=True)
    courses_data = CourseSerializer(courses, many = True)
    print(courses)
    return Response(courses_data.data)


@api_view(['GET'])
def getMentorCourse(request,pk):
    course_obj = course.objects.filter(course_id = pk, islive=True, isonetoone=True)
    instructor_obj = course_obj[0].instructor
    instructor_data = UserForCourseSerializer(instructor_obj)
    courses_data = CourseSerializer(course_obj[0], many = False)
    video_ids = video.objects.filter(course_id = pk)
    video_details = dict()
    for c in range(0, len(video_ids)):
        print(c)
        video_details[c] = video.objects.filter(video_id = video_ids[c].video_id).values()[0]
    return Response({'courses_details':courses_data.data, 'instructor_details':instructor_data.data , 'video_details': video_details})

    