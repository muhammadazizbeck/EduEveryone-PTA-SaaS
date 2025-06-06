from django.shortcuts import render,get_object_or_404
from users.serializers import RegisterStepOneSerializer,RegisterStepTwoSerializer,RegisterStepThreeSerializer,\
LoginSerializer
from users.models import CustomUser

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class RegisterStepOneAPIView(APIView):
    def post(self,request):
        serializer = RegisterStepOneSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response = {
                "code":201,
                'message':"Ro'yhatdan o'tishning birinchi bosqichi yakunlandi",
                'user_id':user.id,
                "data":serializer.data
            }
            return Response(response,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class RegisterStepTwoAPIView(APIView):
    def patch(self,request,user_id):
        user = get_object_or_404(CustomUser,id=user_id)
        serializer = RegisterStepTwoSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "code":200,
                "message":"Ro'yhatdan o'tishning ikkinchi bosqichi yakunlandi",
                "data":serializer.data
            }
            return Response(response,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class RegisterStepThreeAPIView(APIView):
    def patch(self,request,user_id):
        user = get_object_or_404(CustomUser,id=user_id)
        serializer = RegisterStepThreeSerializer(user,data=request.data,partial=True,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            response = {
                "code":200,
                "message":"Ro'yhatdan o'tish to'liq yakunlandi",
                "data":serializer.data
            }
            return Response(response,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class LoginAPIView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'code':200,
                "message":"Muvaffaqiyatli tizimga kirildi",
                'data':serializer.data
            }
            return Response(response,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
