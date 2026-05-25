from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
    

class Users(AbstractBaseUser, PermissionsMixin):

    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'
        CEO = 'ceo', 'CEO'

    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=Roles.choices, default=Roles.USER)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    
    objects = UserManager()
    
    def __str__(self):
        return f"{self.email} {self.role}"


    def __repr__(self):
        return f"{self.email} {self.role}"
    
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
