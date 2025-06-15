from rest_framework import serializers,status,permissions

from courses.models import Course,Lesson,Submission

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'image', 'level', 'author']