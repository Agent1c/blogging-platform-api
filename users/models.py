from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager,  Group, Permission

class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password):
        if not email:
            raise ValueError('Email is required')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255, null=False)
    username = models.CharField(unique=True, max_length=30)
    # name = models.CharField(max_length=255, blank=True, default='')

    groups = models.ManyToManyField(
        Group,
        related_name='group_custom_user_set',  
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set', 
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
