from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageAPIView.as_view(),name='home-page')
]