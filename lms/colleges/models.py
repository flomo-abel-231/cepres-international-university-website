import os.path
from django.contrib.auth.models import User

from django.db import models
from django.template.defaultfilters import slugify


class Standard (models.Model):
    name = models.CharField(max_length=700, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=700, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Standard, self).save(*args, **kwargs)


def save_course_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split(' . ')[-1]

    # get filename

    if instance.course_id:
        filename = 'Course_Pictures/{}.{}'.format(instance.course_id, ext)
        return os.path.join(upload_to, filename)

class Courses (models.Model):
    course_id = models.CharField(max_length=700, unique=True)
    name = models.CharField(max_length=700)
    slug = models.SlugField(null=True, blank=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='courses')
    image = models.ImageField(upload_to=save_course_image, blank=True, verbose_name='Course Image')
    description = models.TextField(max_length=700, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_id)
        super(Courses, self).save(*args, **kwargs)



def save_lesson_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split(' . ')[-1]

    # get filename

    if instance.lesson_id:
        filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id,instance.lesson_id, ext)
        if os.path.exists(filename):
            new_name = str(instance.lesson_id) + str('1')
            filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id, new_name, ext)
    return os.path.join(upload_to, filename)


class Lesson(models.Model):
    lesson_id = models.CharField(max_length=700, unique=True)
    Standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='lesson')
    name = models.CharField(max_length=700)
    position = models.PositiveSmallIntegerField(verbose_name='Chapter no')
    slug = models.SlugField(null=True, blank=True)
    video = models.FileField(upload_to=save_lesson_files, verbose_name='Video', null=True, blank=True)
    ppt = models.FileField(upload_to=save_lesson_files, verbose_name='Presentation',blank=True, null=True)
    Note =models.FileField(upload_to=save_lesson_files, verbose_name='Note', blank=True, null=True)


    class meta:
        ordering = ['position']


    def __str__(self):
        return self.name

    def save(self, *args , **kwargs):
        self.slug = slugify(self.name)
        super(Lesson, self).save(*args, **kwargs)



