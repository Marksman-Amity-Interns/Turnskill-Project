from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.getRoutes, name="routes"),
    path('courses/',views.getCourses, name="courses"),
    path('courses/<str:pk>/',views.getCourse, name ="course"),
    path('users/',views.getUsers, name ="users"),
    path('users/<str:pk>/',views.getUser, name ="user"),
    path('virtual-classroom/',views.getVirtualCourses, name="virtual-classroom"),
    path('virtual-classroom/<str:pk>/',views.getVirtualCourse, name ="virtual-classroom"),
    path('mentor/',views.getMentorCourses, name="mentor-courses"),
    path('mentor/<str:pk>/',views.getMentorCourse, name ="mentor-course"),
]