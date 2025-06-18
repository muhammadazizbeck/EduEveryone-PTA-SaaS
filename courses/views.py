from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import permissions,status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from courses.models import Course,Submission,Lesson
from courses.serializers import CourseListSerializer,CourseDetailSerializer,LessonDetailSerializer
# Create your views here.

class CourseListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        responses={200: CourseListSerializer()}
    )
    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseListSerializer(courses,many=True)
        response = {
            'code':200,
            'data':serializer.data
        }
        return Response(response,status=status.HTTP_200_OK)

class CourseDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        responses={200: CourseDetailSerializer()}
    )
    def get(self,request,id):
        course = Course.objects.get(id=id)
        serializer = CourseDetailSerializer(course)
        response = {
            'code':200,
            'data':serializer.data
        }
        return Response(response,status=status.HTTP_200_OK)
    
class LessonDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        responses={200:LessonDetailSerializer()}
    )
    def get(self,request,id):
        lesson = Lesson.objects.get(id=id)
        serializer = LessonDetailSerializer(lesson,conttext={'request':request})
        response = {
            'code':200,
            "data":serializer.data
        }
        return Response(response,status=status.HTTP_200_OK)
    
#ddd
    
