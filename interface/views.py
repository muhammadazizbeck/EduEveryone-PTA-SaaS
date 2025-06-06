from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HomePageAPIView(APIView):
    def get(self,request):
        return Response({'message':"Welcome to our EduEveryone API Section"})
