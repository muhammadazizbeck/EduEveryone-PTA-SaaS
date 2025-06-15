from django.urls import path
from . import views

urlpatterns = [
    path("course-list/",views.CourseListAPIView.as_view(),name='course-list'),
    path("course-detail/<int:id>/",views.CourseDetailAPIView.as_view(),name='course-detail'),
    path("lesson-detail/<int:id>/",views.LessonDetailAPIView.as_view(),name='lesson-detail')
]