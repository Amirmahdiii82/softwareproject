from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('user', 'User'),
        ('guest', 'Guest'),
    )
    
    phone_number = models.CharField(max_length=15, unique=True, null=True)  # اضافه کردن null=True
    role = models.CharField(max_length=20, choices=ROLES, default='user')

    def is_super_admin(self):
        return self.role == 'super_admin'

    def is_admin(self):
        return self.role == 'admin'