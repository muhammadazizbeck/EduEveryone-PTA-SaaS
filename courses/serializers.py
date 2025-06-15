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

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ("id",'file',"submitted_at","grade","feedback")

class LessonDetailSerializer(serializers.ModelSerializer):
    submission = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ["id",'title','instruction','video','assignment_file','order','submission']

    def get_submission(self,obj):
        user = self.context["request"].user
        if user.is_authenticated and user.is_student:
            submission = Submission.objects.filter(student=user,lesson=obj).first()
            if submission:
                return SubmissionSerializer(submission).data
        return None

