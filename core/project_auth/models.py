from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# Create your models here.


class CustomUser(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    is_teacher = models.BooleanField()
    is_student = models.BooleanField()

    def __str__(self):
        if self.is_teacher:
            return self.first_name + "Teacher"
        else:
            return self.first_name + "Student"

# class Teacher(models.Model):
#     name = models.CharField(max_length=50)
#     subject = models.CharField(max_length=30)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#     # class Meta:
#     #     permissions = [('can_add_teacher', 'can add new teacher')]
#
#
# class Student(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='student')
#     password = models.CharField(max_length=50)
#
#     # class Meta:
#     #     permissions = [
#     #         ('can_add_student', 'can add new student'),
#     #         ('can_view_student', 'can view student'),
#     #         ('can_change_student', 'can change student'),
#     #     ]
#
#     def __str__(self):
#         return self.name
#
