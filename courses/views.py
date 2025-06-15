from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import permissions,status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from courses.models import Course
from courses.serializers import CourseListSerializer
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
    
