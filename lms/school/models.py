from django.db import models
from django.contrib.auth.models import User

import os
def path_and_rename(instance, filename):
    upload_to ='Images/'
    ext = filename.split('.')[-1]

    if instance.user.username:
        filename = 'User_Profile_Picture/{}.{}'.format(instance.user.username, ext)
        return os.path.join(upload_to, filename)

class user_profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.CharField(max_length=700, blank=True)

    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="profile_picture", blank=True)

    teacher = "teacher"
    student = "student"
    parent = "parent"

    user_types = [
        (student, "student"),
        (parent, "parent"),
        (teacher, "teacher")
    ]
    user_type = models.CharField(max_length=12, choices=user_types,default=student)


    def __str__(self):
        return self.user.username


