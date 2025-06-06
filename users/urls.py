from django.urls import path
from . import views

urlpatterns = [
    path('auth/login/',views.LoginAPIView.as_view(),name='login'),
    path('auth/register/step1/',views.RegisterStepOneAPIView.as_view(),name='register-step1'),
    path('auth/register/step2/<int:user_id>/',views.RegisterStepTwoAPIView.as_view(),name='register-step2'),
    path('auth/register/step3/<int:user_id>/',views.RegisterStepThreeAPIView.as_view(),name='register-step2'),
]