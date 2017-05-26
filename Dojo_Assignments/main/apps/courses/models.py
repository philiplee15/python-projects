from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def query(self):
        pass
class CourseName(models.Model):
    name = models.CharField(max_length=30,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
class Description(models.Model):
    desc = models.CharField(max_length=300,null=True)
    course = models.OneToOneField(CourseName)
