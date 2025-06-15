from django.urls import path
from . import views

urlpatterns = [
    path('course-list/',views.CourseListAPIView.as_view(),name='course-list')
]