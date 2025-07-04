from rest_framework import serializers
from users.models import CustomUser
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from users.exceptions import InvalidPasswordException,PasswordMismatchException,EmailAlreadyExistsException,DisabilityRequiredException, \
UserNotFoundException,NewPasswordMismatchException,OldPasswordIncorrectException


class RegisterStepOneSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=50,required=True,write_only=True)
    password2 = serializers.CharField(max_length=50,required=True,write_only=True)

    class Meta:
        model = CustomUser
        fields = ['full_name','email','password1','password2']

    def validate(self,data):
        if data['password1'] != data['password2']:
            raise PasswordMismatchException()
        return data
    
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            return EmailAlreadyExistsException()
        return value
    
    def create(self, validated_data):
        password = validated_data.pop("password1")
        validated_data.pop("password2")
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

class RegisterStepTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_type']
    
class RegisterStepThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['disability_type']

    def validate(self, data):
        user = self.instance  

        if user.user_type == 'student' and not data.get('disability_type'):
            raise DisabilityRequiredException()
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50, required=True, write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = CustomUser.objects.get(email=email)

        except CustomUser.DoesNotExist:
            raise UserNotFoundException()
        
        if not user.check_password(password):
            raise InvalidPasswordException()

        refresh = RefreshToken.for_user(user)

        return {
            "user_id":user.id,
            'email': user.email,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            "full_name": user.full_name,
            "user_type": user.user_type,
            "disability_type":user.disability_type
        }

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True,max_length=50,required=True)
    new_password = serializers.CharField(write_only=True,required=True,max_length=50)
    confirm_new_password = serializers.CharField(write_only=True,required=True,max_length=50)

    def validate(self,data):
        if data["new_password"]!=data['confirm_new_password']:
            raise NewPasswordMismatchException()
        return data
    
    def validate_old_password(self,attrs):
        user = self.context['request'].user
        if not user.check_password(attrs):
            raise OldPasswordIncorrectException()
        return attrs
    
    def save(self,**kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id","email","full_name")
        read_only_fields = ("id","email")

            
    
        