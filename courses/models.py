from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import CustomUser

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images')
    level = models.PositiveIntegerField()
    author = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,related_name='courses',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons')
    title = models.CharField(max_length=50)
    instruction = models.TextField()
    video = models.FileField(upload_to='lesson_videos/')
    assignment_file = models.FileField(upload_to="assignment_files/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title}-{self.title}"


class Submission(models.Model):
    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    file = models.FileField(upload_to='submission_files')
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    feedback = models.TextField(blank=True,null=True)

    class Meta:
        unique_together = ('student','lesson')

    
