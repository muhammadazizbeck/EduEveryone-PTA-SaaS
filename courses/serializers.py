from rest_framework import serializers,status,permissions

from courses.models import Course,Lesson,Submission

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'image', 'level', 'author']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'instruction', 'video', 'assignment_file', 'order']

class CourseDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True,read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'image', 'level', 'author', 'created_at', 'lessons']
