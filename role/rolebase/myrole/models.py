from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('hod', 'Head of Department'),
        ('principal', 'Principal'),
        ('student', 'Student'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True, blank=True)

    class Meta:
        db_table = 'custom_user'

class Hod(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'role': 'hod'})
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Principal(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'role': 'principal'})
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'role': 'student'})
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'role': 'staff'})
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name
