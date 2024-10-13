from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Note(models.Model):
    text = models.CharField(verbose_name='Text', max_length=250)
    created_date = models.DateTimeField(verbose_name='Date Created', auto_now=True)
    author = models.CharField(verbose_name='Author', max_length=100)
