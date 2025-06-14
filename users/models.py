from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email manzili kiritilishi shart')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser is_staff bo\'lishi shart')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser is_superuser bo\'lishi shart')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    USER_TYPE_CHOISES = (
        ('student',"O'quvchi"),
        ("teacher","O'qituvchi"),
    )

    DISABILITY_TYPE_CHOISES = (
        ("A1","Eshitmaydigan"),
        ("A2","Jismoniy nogiron"),
    )

    username = None
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20,choices=USER_TYPE_CHOISES,blank=True,null=True)
    disability_type = models.CharField(max_length=20,choices=DISABILITY_TYPE_CHOISES,blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.full_name} ({self.email})"

