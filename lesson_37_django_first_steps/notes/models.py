from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(verbose_name='Title', max_length=250, default="")

    def __str__(self):
        return self.title


class Note(models.Model):
    text = models.CharField(verbose_name='Text', max_length=250)
    created_date = models.DateTimeField(verbose_name='Date Created', auto_now=True)
    author = models.CharField(verbose_name='Author', max_length=100)
    title = models.CharField(verbose_name='Title', max_length=250, default="")
    reminder = models.DateTimeField(verbose_name='Reminder', default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=None)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.title}: {self.text}"
