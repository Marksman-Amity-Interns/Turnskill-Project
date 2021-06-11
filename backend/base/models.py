from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class skill_course(models.Model):
    course_id = models.AutoField(primary_key=True, editable=False)
    course_title = models.CharField(max_length=200, null=True, blank=True)
    course_category = models.CharField(max_length=200, null=True, blank=True)
    course_image = models.ImageField(null=True, blank=True)